## Wireshark

Kali 升级之后启动 Wireshark 报段错误

```
# vim /usr/share/wireshark/init.lua

倒数第二行
dofile(DATA_DIR.."console.lua")
>>
--dofile(DATA_DIR.."console.lua")
```
