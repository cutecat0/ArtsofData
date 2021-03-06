#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.getLogger().setLevel(logging.INFO)


def test():
    """
    TCP/IP protocol
    only tag is IP address on the Internet to transfer message between two or more computers
    reference： https://www.liaoxuefeng.com/wiki/1016959663602400/1017787663253120
    IP Address actually is the net interface of computer, usually it's network interface card '网卡'
    P协议负责把数据从一台计算机通过网络发送到另一台计算机。
    数据被分割成一小块一小块，然后通过IP包发送出去。
    由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
    IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。

    IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。
    IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于2001:0db8:85a3:0042:1000:8a2e:0370:7334。

    TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
    TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

    许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

    一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。

    端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
    一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。
    每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

    一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口
    :return:
    """