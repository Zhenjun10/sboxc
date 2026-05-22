# @brief: 默认全局代理
# @version: 1.12.0
# @author: cheremace

config = {
# 配置文件参考资料 https://sing-box.sagernet.org/zh/configuration/
  "log": {
    "disabled": False,
    "level": "info",
    "output": "",
    "timestamp": True
  },
  "experimental": {
    "clash_api": {
      "external_controller": "127.0.0.1:20123",  # 访问 127.0.0.1:20123/ui
      "external_ui": "./ui",
      "external_ui_download_url": "",  # git clone https://github.com/metacubex/metacubexd.git -b gh-pages ui
      "external_ui_download_detour": "手动选择",
      "secret": "LAk8yWcj#njTZ%QZ2a",
      "default_mode": "rule",
      "access_control_allow_origin": [
        "*"
      ],
      "access_control_allow_private_network": False
    },
    "cache_file": {
      "enabled": True,
      "path": "cache.db",
      "cache_id": "",
      "store_fakeip": False,
      "store_rdrc": True,
      "rdrc_timeout": "7d"
    }
  },
  "inbounds": [
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "0.0.0.0",
      "listen_port": 21765,
      "tcp_fast_open": False,
      "tcp_multi_path": False,
      "udp_fragment": False
    },
  ],
  "outbounds": [
    {
      "type": "selector",
      "tag": "手动选择",
      "interrupt_exist_connections": True,
      "outbounds": []
    },
  ],
  "route": {
    "auto_detect_interface": True,
    "final": "手动选择",
    "default_domain_resolver": {  # 解析 节点 域名策略, 可以被 outbound.domain_resolver 覆盖
      "server": "Local-DNS",
      "strategy": "ipv4_only",  # 解决 empty result (cached) 错误 #3461
      "rewrite_ttl": 60,
      # "client_subnet": "1.1.1.1"
    }
  },
  "dns": {
    "servers": [
      {
        "tag": "Local-DNS",
        "type": "https",
        "domain_resolver": "Local-DNS-Resolver",
        "server": "223.5.5.5",
        "path": "/dns-query"
      },
      {
        "tag": "Local-DNS-Resolver",
        "type": "udp",
        "server": "223.5.5.5"
      },
      {
        "tag": "Remote-DNS",
        "type": "tls",
        "detour": "手动选择",
        "domain_resolver": "Remote-DNS-Resolver",
        "server": "8.8.8.8"
      },
      {
        "tag": "Remote-DNS-Resolver",
        "type": "udp",
        "detour": "手动选择",
        "server": "8.8.8.8"
      }
    ],
    "final": "Remote-DNS",
    "strategy": "ipv4_only",  # 解析 所有 域名策略
    "disable_cache": False,
    "disable_expire": False,
    "independent_cache": False,
  }
}
