@echo off
"C:\Portable\SingBox\bin\sing-box.exe" rule-set compile --output .\bin\reject.srs .\build\reject.json
"C:\Portable\SingBox\bin\sing-box.exe" rule-set compile --output .\bin\direct.srs .\build\direct.json
"C:\Portable\SingBox\bin\sing-box.exe" rule-set compile --output .\bin\proxy.srs .\build\proxy.json
echo 转换完成！
