## HTTrack

https://www.httrack.com/

安装及使用
```
$ brew install httrack
$ httrack "http://www.abc.net/" -O "/tmp/www.abc.net" "+*.abc.net/*" -v
```

或者直接使用`wget`
```
$ wget -m "http://www.abc.net/"
$ wget -m -e robots=off -k -E "http://www.abc.net/"
```

`wget`参数解释
```
-m              //镜像，就是整站抓取 
-e robots=off   //忽略robots协议 
-k              //将绝对URL链接转换为本地相对URL 
-E              //将所有text/html文档以.html扩展名保存
```
