# @version: 1.12.0
# @author: cheremace

config = {
# 配置文件参考资料 https://sing-box.sagernet.org/zh/configuration/
  "log": {
    "disabled": False,
    "level": "debug",
    "output": "",
    "timestamp": False
  },
  "experimental": {
    "clash_api": {
      "external_controller": "127.0.0.1:20123",
      "external_ui": "",
      "external_ui_download_url": "",
      "external_ui_download_detour": "🎯 全球直连",
      "secret": "ID_7oqrfbpd",
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
      "store_fakeip": True,
      "store_rdrc": True,
      "rdrc_timeout": "7d"
    }
  },
  "inbounds": [
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "127.0.0.1",
      "listen_port": 20122,
      "tcp_fast_open": False,
      "tcp_multi_path": False,
      "udp_fragment": False
    },
    {
      "type": "tun",
      "tag": "tun-in",
      "interface_name": "",
      "address": [
        "172.18.0.1/30",
        "fdfe:dcba:9876::1/126"
      ],
      "mtu": 9000,
      "auto_route": True,
      "strict_route": True,
      "endpoint_independent_nat": False,
      "stack": "mixed"
    }
  ],
  "outbounds": [
    {
      "type": "selector",
      "tag": "🚀 节点选择",
      "interrupt_exist_connections": True,
      "outbounds": [
        "🎈 自动选择",
        "🇪🇸 西班牙 01",
        "🇬🇧 英国 01",
        "🇬🇧 英国 02",
        "🇭🇰 香港 01",
        "🇭🇰 香港 02",
        "🇭🇰 香港 03",
        "🇭🇰 香港 04",
        "🇭🇰 香港 05",
        "🇭🇰 香港 06",
        "🇭🇰 香港 07",
        "🇭🇰 香港 08",
        "🇭🇰 香港 09",
        "🇭🇰 香港 10",
        "🇭🇰 香港 11",
        "🇭🇰 香港 12",
        "🇭🇰 香港 13",
        "🇭🇰 香港 14",
        "🇭🇰 香港 15",
        "🇯🇵 日本 01",
        "🇯🇵 日本 02",
        "🇯🇵 日本 03",
        "🇯🇵 日本 04",
        "🇯🇵 日本 05",
        "🇯🇵 日本 06",
        "🇯🇵 日本 07",
        "🇯🇵 日本 08",
        "🇯🇵 日本 09",
        "🇯🇵 日本 10",
        "🇲🇾 马来西亚 01",
        "🇷🇺 俄罗斯 01",
        "🇸🇬 新加坡 01",
        "🇸🇬 新加坡 02",
        "🇸🇬 新加坡 03",
        "🇸🇬 新加坡 04",
        "🇸🇬 新加坡 05",
        "🇸🇬 新加坡 06",
        "🇸🇬 新加坡 07",
        "🇸🇬 新加坡 08",
        "🇸🇬 新加坡 09",
        "🇸🇬 新加坡 10",
        "🇹🇷 土耳其 01",
        "🇹🇼 台湾 01",
        "🇹🇼 台湾 02",
        "🇹🇼 台湾 03",
        "🇹🇼 台湾 04",
        "🇹🇼 台湾 05",
        "🇺🇸 美国 01",
        "🇺🇸 美国 02",
        "🇺🇸 美国 03",
        "🇺🇸 美国 04",
        "🇺🇸 美国 05",
        "🇺🇸 美国 06",
        "🇺🇸 美国 07",
        "🇺🇸 美国 08",
        "距离下次重置剩余：26 天",
        "套餐到期：2025-09-11"
      ]
    },
    {
      "type": "urltest",
      "tag": "🎈 自动选择",
      "url": "https://www.gstatic.com/generate_204",
      "interval": "3m",
      "tolerance": 150,
      "interrupt_exist_connections": True,
      "outbounds": [
        "🇪🇸 西班牙 01",
        "🇬🇧 英国 01",
        "🇬🇧 英国 02",
        "🇭🇰 香港 01",
        "🇭🇰 香港 02",
        "🇭🇰 香港 03",
        "🇭🇰 香港 04",
        "🇭🇰 香港 05",
        "🇭🇰 香港 06",
        "🇭🇰 香港 07",
        "🇭🇰 香港 08",
        "🇭🇰 香港 09",
        "🇭🇰 香港 10",
        "🇭🇰 香港 11",
        "🇭🇰 香港 12",
        "🇭🇰 香港 13",
        "🇭🇰 香港 14",
        "🇭🇰 香港 15",
        "🇯🇵 日本 01",
        "🇯🇵 日本 02",
        "🇯🇵 日本 03",
        "🇯🇵 日本 04",
        "🇯🇵 日本 05",
        "🇯🇵 日本 06",
        "🇯🇵 日本 07",
        "🇯🇵 日本 08",
        "🇯🇵 日本 09",
        "🇯🇵 日本 10",
        "🇲🇾 马来西亚 01",
        "🇷🇺 俄罗斯 01",
        "🇸🇬 新加坡 01",
        "🇸🇬 新加坡 02",
        "🇸🇬 新加坡 03",
        "🇸🇬 新加坡 04",
        "🇸🇬 新加坡 05",
        "🇸🇬 新加坡 06",
        "🇸🇬 新加坡 07",
        "🇸🇬 新加坡 08",
        "🇸🇬 新加坡 09",
        "🇸🇬 新加坡 10",
        "🇹🇷 土耳其 01",
        "🇹🇼 台湾 01",
        "🇹🇼 台湾 02",
        "🇹🇼 台湾 03",
        "🇹🇼 台湾 04",
        "🇹🇼 台湾 05",
        "🇺🇸 美国 01",
        "🇺🇸 美国 02",
        "🇺🇸 美国 03",
        "🇺🇸 美国 04",
        "🇺🇸 美国 05",
        "🇺🇸 美国 06",
        "🇺🇸 美国 07",
        "🇺🇸 美国 08",
        "距离下次重置剩余：26 天",
        "套餐到期：2025-09-11"
      ]
    },
    {
      "type": "direct",
      "tag": "🎯 全球直连"
    },
    {
      "type": "selector",
      "tag": "🐟 漏网之鱼",
      "interrupt_exist_connections": True,
      "outbounds": [
        "🚀 节点选择",
        "🎯 全球直连"
      ]
    },
    {
      "type": "selector",
      "tag": "GLOBAL",
      "interrupt_exist_connections": True,
      "outbounds": [
        "🚀 节点选择",
        "🎈 自动选择",
        "🎯 全球直连",
        "🐟 漏网之鱼"
      ]
    },
    {
      "tag": "🇪🇸 西班牙 01",
      "type": "shadowsocks",
      "server": "tqt-tt-dl.51feitu.com",
      "server_port": 19408,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇬🇧 英国 01",
      "type": "shadowsocks",
      "server": "tqt-hk01-dl.51feitu.com",
      "server_port": 27801,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇬🇧 英国 02",
      "type": "shadowsocks",
      "server": "tqt-tt-dl.51feitu.com",
      "server_port": 19406,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 01",
      "type": "shadowsocks",
      "server": "tqt-hk01-dl.51feitu.com",
      "server_port": 27801,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 02",
      "type": "vmess",
      "server": "tqt-hk02-dl.51feitu.com",
      "server_port": 27802,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk02-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 03",
      "type": "shadowsocks",
      "server": "tqt-hk03-dl.51feitu.com",
      "server_port": 27803,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 04",
      "type": "vmess",
      "server": "tqt-hk04-dl.51feitu.com",
      "server_port": 27804,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk04-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 05",
      "type": "shadowsocks",
      "server": "tqt-hk05-dl.51feitu.com",
      "server_port": 27805,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 06",
      "type": "vmess",
      "server": "tqt-hk-vip-dl.51feitu.com",
      "server_port": 31006,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 07",
      "type": "shadowsocks",
      "server": "tqt-hk-vip-dl.51feitu.com",
      "server_port": 31007,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 08",
      "type": "vmess",
      "server": "tqt-hk-vip-dl.51feitu.com",
      "server_port": 31008,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 09",
      "type": "shadowsocks",
      "server": "tqt-hk-vip-dl.51feitu.com",
      "server_port": 31009,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 10",
      "type": "vmess",
      "server": "tqt-hk-vip-dl.51feitu.com",
      "server_port": 31010,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 11",
      "type": "shadowsocks",
      "server": "tqt-hk11-dl.51feitu.com",
      "server_port": 27811,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 12",
      "type": "vmess",
      "server": "tqt-hk12-dl.51feitu.com",
      "server_port": 27812,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk12-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 13",
      "type": "shadowsocks",
      "server": "tqt-hk13-dl.51feitu.com",
      "server_port": 27813,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇭🇰 香港 14",
      "type": "vmess",
      "server": "tqt-hk14-dl.51feitu.com",
      "server_port": 27814,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-hk14-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇭🇰 香港 15",
      "type": "shadowsocks",
      "server": "tqt-hk15-dl.51feitu.com",
      "server_port": 27815,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 01",
      "type": "shadowsocks",
      "server": "tqt-jp01-dl.51feitu.com",
      "server_port": 43711,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 02",
      "type": "vmess",
      "server": "tqt-jp02-dl.51feitu.com",
      "server_port": 43702,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-jp02-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇯🇵 日本 03",
      "type": "shadowsocks",
      "server": "tqt-jp03-dl.51feitu.com",
      "server_port": 43703,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 04",
      "type": "vmess",
      "server": "tqt-jp02-dl.51feitu.com",
      "server_port": 43714,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-jp02-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇯🇵 日本 05",
      "type": "shadowsocks",
      "server": "tqt-jp05-dl.51feitu.com",
      "server_port": 43705,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 06",
      "type": "vmess",
      "server": "tqt-jp-vip-dl.51feitu.com",
      "server_port": 33006,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-jp-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇯🇵 日本 07",
      "type": "shadowsocks",
      "server": "tqt-jp-vip-dl.51feitu.com",
      "server_port": 33007,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 08",
      "type": "vmess",
      "server": "tqt-jp-vip-dl.51feitu.com",
      "server_port": 33008,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-jp-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇯🇵 日本 09",
      "type": "shadowsocks",
      "server": "tqt-jp-vip-dl.51feitu.com",
      "server_port": 33009,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇯🇵 日本 10",
      "type": "vmess",
      "server": "tqt-jp-vip-dl.51feitu.com",
      "server_port": 33010,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-jp-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇲🇾 马来西亚 01",
      "type": "shadowsocks",
      "server": "tqt-tt-dl.51feitu.com",
      "server_port": 13091,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇷🇺 俄罗斯 01",
      "type": "shadowsocks",
      "server": "tqt-tt-dl.51feitu.com",
      "server_port": 13491,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 01",
      "type": "shadowsocks",
      "server": "tqt-sg01-dl.51feitu.com",
      "server_port": 42801,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 02",
      "type": "vmess",
      "server": "tqt-sg02-dl.51feitu.com",
      "server_port": 42802,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-sg02-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇸🇬 新加坡 03",
      "type": "shadowsocks",
      "server": "tqt-sg03-dl.51feitu.com",
      "server_port": 42803,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 04",
      "type": "vmess",
      "server": "tqt-sg04-dl.51feitu.com",
      "server_port": 42814,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-sg04-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇸🇬 新加坡 05",
      "type": "shadowsocks",
      "server": "tqt-sg05-dl.51feitu.com",
      "server_port": 42805,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 06",
      "type": "vmess",
      "server": "tqt-sg-vip-dl.51feitu.com",
      "server_port": 32006,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-sg-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇸🇬 新加坡 07",
      "type": "shadowsocks",
      "server": "tqt-sg-vip-dl.51feitu.com",
      "server_port": 32007,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 08",
      "type": "vmess",
      "server": "tqt-sg-vip-dl.51feitu.com",
      "server_port": 32008,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-sg-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇸🇬 新加坡 09",
      "type": "shadowsocks",
      "server": "tqt-sg-vip-dl.51feitu.com",
      "server_port": 32009,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇸🇬 新加坡 10",
      "type": "vmess",
      "server": "tqt-sg-vip-dl.51feitu.com",
      "server_port": 32010,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-sg-vip-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇹🇷 土耳其 01",
      "type": "shadowsocks",
      "server": "tqt-tt-dl.51feitu.com",
      "server_port": 13092,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇹🇼 台湾 01",
      "type": "shadowsocks",
      "server": "tqt-tw01-dl.51feitu.com",
      "server_port": 52416,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇹🇼 台湾 02",
      "type": "shadowsocks",
      "server": "tqt-tw02-dl.51feitu.com",
      "server_port": 52417,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇹🇼 台湾 03",
      "type": "shadowsocks",
      "server": "tqt-tw03-dl.51feitu.com",
      "server_port": 52418,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇹🇼 台湾 04",
      "type": "shadowsocks",
      "server": "tqt-tw-vip-dl.51feitu.com",
      "server_port": 35004,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇹🇼 台湾 05",
      "type": "shadowsocks",
      "server": "tqt-tw-vip-dl.51feitu.com",
      "server_port": 35005,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 01",
      "type": "shadowsocks",
      "server": "tqt-us01-dl.51feitu.com",
      "server_port": 47969,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 02",
      "type": "vmess",
      "server": "tqt-us02-dl.51feitu.com",
      "server_port": 30820,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-us02-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇺🇸 美国 03",
      "type": "shadowsocks",
      "server": "tqt-us03-dl.51feitu.com",
      "server_port": 23199,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 04",
      "type": "vmess",
      "server": "tqt-us04-dl.51feitu.com",
      "server_port": 44948,
      "uuid": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe",
      "security": "auto",
      "alter_id": 0,
      "transport": {
        "type": "ws",
        "headers": {
          "Host": "tqt-us04-dl.51feitu.com"
        },
        "max_early_data": None,
        "path": "/"
      }
    },
    {
      "tag": "🇺🇸 美国 05",
      "type": "shadowsocks",
      "server": "tqt-us05-dl.51feitu.com",
      "server_port": 44949,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 06",
      "type": "shadowsocks",
      "server": "tqt-us-vip-dl.51feitu.com",
      "server_port": 34006,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 07",
      "type": "shadowsocks",
      "server": "tqt-us-vip-dl.51feitu.com",
      "server_port": 34007,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "🇺🇸 美国 08",
      "type": "shadowsocks",
      "server": "tqt-us-vip-dl.51feitu.com",
      "server_port": 34008,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "距离下次重置剩余：26 天",
      "type": "shadowsocks",
      "server": "tqt-hk01-dl.51feitu.com",
      "server_port": 27801,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    },
    {
      "tag": "套餐到期：2025-09-11",
      "type": "shadowsocks",
      "server": "tqt-hk01-dl.51feitu.com",
      "server_port": 27801,
      "method": "chacha20-ietf-poly1305",
      "password": "6a2b4735-ba01-41d4-9bb6-86afdb6027fe"
    }
  ],
  "route": {
    "rules": [
      {
        "action": "route",
        "rule_set": [
          "PROXY"
        ],
        "outbound": "🚀 节点选择"
      },
      {
        "action": "reject",
        "rule_set": [
          "REJECT"
        ]
      },
      {
        "action": "route",
        "rule_set": [
          "DIRECT"
        ],
        "outbound": "🎯 全球直连"
      },
      {
        "action": "sniff",
        "inbound": "tun-in"
      },
      {
        "action": "hijack-dns",
        "protocol": "dns"
      },
      {
        "action": "route",
        "clash_mode": "direct",
        "outbound": "🎯 全球直连"
      },
      {
        "action": "route",
        "clash_mode": "global",
        "outbound": "GLOBAL"
      },
      {
        "action": "reject",
        "protocol": "quic"
      },
      {
        "action": "reject",
        "rule_set": [
          "Category-Ads"
        ]
      },
      {
        "action": "route",
        "rule_set": [
          "GeoSite-Private"
        ],
        "outbound": "🎯 全球直连"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoSite-CN"
        ],
        "outbound": "🎯 全球直连"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoIP-Private"
        ],
        "outbound": "🎯 全球直连"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoIP-CN"
        ],
        "outbound": "🎯 全球直连"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoLocation-!CN"
        ],
        "outbound": "🚀 节点选择"
      }
    ],
    "rule_set": [
      {
        "tag": "PROXY",
        "type": "local",
        "path": "../rulesets/PROXY.json",
        "format": "source"
      },
      {
        "tag": "REJECT",
        "type": "local",
        "path": "../rulesets/REJECT.json",
        "format": "source"
      },
      {
        "tag": "DIRECT",
        "type": "local",
        "path": "../rulesets/DIRECT.json",
        "format": "source"
      },
      {
        "tag": "Category-Ads",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-ads-all.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      },
      {
        "tag": "GeoIP-Private",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/private.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      },
      {
        "tag": "GeoSite-Private",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/private.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      },
      {
        "tag": "GeoIP-CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/cn.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      },
      {
        "tag": "GeoSite-CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/cn.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      },
      {
        "tag": "GeoLocation-!CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/geolocation-!cn.srs",
        "format": "binary",
        "download_detour": "🎯 全球直连"
      }
    ],
    "auto_detect_interface": True,
    "final": "🐟 漏网之鱼"
  },
  "dns": {
    "servers": [
      {
        "tag": "Local-DNS",
        "address": "https://223.5.5.5/dns-query",
        "address_resolver": "Local-DNS-Resolver",
        "detour": "🎯 全球直连"
      },
      {
        "tag": "Local-DNS-Resolver",
        "address": "223.5.5.5",
        "detour": "🎯 全球直连"
      },
      {
        "tag": "Remote-DNS",
        "address": "tls://8.8.8.8",
        "address_resolver": "Remote-DNS-Resolver",
        "detour": "🚀 节点选择"
      },
      {
        "tag": "Remote-DNS-Resolver",
        "address": "8.8.8.8",
        "detour": "🚀 节点选择"
      }
    ],
    "rules": [
      {
        "action": "route",
        "server": "Local-DNS",
        "outbound": "any"
      },
      {
        "action": "route",
        "server": "Local-DNS",
        "clash_mode": "direct"
      },
      {
        "action": "route",
        "server": "Remote-DNS",
        "clash_mode": "global"
      },
      {
        "action": "route",
        "server": "Local-DNS",
        "rule_set": [
          "GeoSite-CN"
        ]
      },
      {
        "action": "route",
        "server": "Remote-DNS",
        "rule_set": [
          "GeoLocation-!CN"
        ]
      }
    ],
    "fakeip": {
      "enabled": False,
      "inet4_range": "198.18.0.0/15",
      "inet6_range": "fc00::/18"
    },
    "disable_cache": False,
    "disable_expire": False,
    "independent_cache": False,
    "final": "Remote-DNS"
  }

}