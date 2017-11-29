## 常用库
https://github.com/requests/requests

https://github.com/kennethreitz/grequests


## web应用主要面临的安全问题：

1.数据篡改

2.数据窃取

3.重放攻击

4.非法参数提交 （SQL注入,XSS等）

## 漏洞列表

### 重置密码漏洞

- 背景介绍

一般的密码重置的设计都是分为以下四步：

1. 输入账户名
2. 验证身份
3. 重置密码
4. 完成

- 漏洞类型
1. 手机重置
2. 邮箱重置

- 破解场景
1. 爆破
手机验证，验证码没有验证次数限制（第2步）
2. 伪造签名
邮箱验证，重置链接签名设计过于简单（第2步）
3. 偷梁换柱
由于设计缺陷，第3步没有持续验证身份，可构造链接，直接重置用户密码

- 防御措施
1. 对每个步骤，所有参数加签名，后端严格校验合法性。
2. 可以对尝试攻击（签名校验失败）的用户，记录IP，cookie等信息，主动防御。

### SQL 注入



### XSS
跨站脚本

- 漏洞类型
1、反射型 XSS
```
payload："><script>alert("XSS")</script>
```
2、存储型 XSS
```
payload：">
```

- 防御措施


### CSRF
跨站请求伪造

- 攻击方式：
    利用用户身份执行非法请求（在用户浏览器端发起特定请求）
- 防御策略：
    通常使用csrf_token防御



### Cross-Frame Scripting (XFS) 

http://tinyurl.com/anticlickjack


### 模板注入

tplmap

[项目地址](https://github.com/epinna/tplmap)


## 常用工具

- BurpSuite
- SqlMap
- NMap


## 渗透演练

[Damn Vulnerable Web Application (DVWA)](http://www.dvwa.co.uk/)

[项目地址](https://github.com/ethicalhack3r/DVWA)


## 参考资料

http://websec.ca/kb/sql_injection
