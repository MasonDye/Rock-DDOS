# ROCK-DDOS

[**English**](README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**中文简体**](README_ZH-CN.md)

这个项目提供了一个简化的多代理服务器CC攻击模拟器，用于教育和研究目的。请注意，任何形式的DDoS攻击都是非法行为，务必遵守法律和道德规范。

## 功能

- 支持CC,UDP,TCP,NTP,ARP洪流攻击，部分支持代理（反射服务器）

- 使用HTTP或SOCKS代理进行多IP的CC洪流攻击模拟
- 支持从文件中读取代理列表
- 支持动态更新代理池
- 并发发送请求

## 安装

```bash
pip install requests
pip install scapy
```

如果你在Windows下运行，你需要安装npcap或者winpcap。

## 用法

1. **编辑Python代码**：
   
   - 修改目标服务器以及更多参数，如：
     ```python
     target_ip = "10.192.162.1"   # 替换为目标IP地址
     target_port = 80  # 替换为目标端口
     packet_size = 1024  # 每个数据包的大小
     ```
2. **运行脚本**：
   
   - 完成修改代码中的中的`target_url`、`num_threads`和`num_requests`等变量，设置目标URL、线程数量和请求数量。
   - 运行命令：
     
     ```bash
     python cc_attack.py
     ```

## 注意事项

- 任何形式的DDoS攻击都是非法行为，务必遵守法律和道德规范。
- 这个项目仅用于教育和研究目的，不应用于任何非法活动。

## 贡献

欢迎提交Pull Request来改进这个项目。

## 许可证

MIT License

```
请注意，这段文档只是为了演示HTTP请求的发送过程，实际的DDoS攻击需要更复杂的工具和策略来实现。任何形式的DDoS攻击都是非法行为，务必遵守法律和道德规范。
```
