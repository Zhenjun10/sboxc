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
      "listen_port": 21764,
      "tcp_fast_open": False,
      "tcp_multi_path": False,
      "udp_fragment": False
    },
    {
      "type": "tun",
      "tag": "tun-in",
      "interface_name": "",
      "address": [
        "10.0.1.1/30"
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
      "tag": "手动选择",
      "interrupt_exist_connections": True,
      "outbounds": [
        "自动选择"
      ]
    },
    {
      "type": "urltest",
      "tag": "自动选择",
      "url": "https://www.gstatic.com/generate_204",
      "interval": "3m",
      "tolerance": 150,
      "interrupt_exist_connections": True,
      "outbounds": []
    },
    {
      "type": "direct",
      "tag": "DIRECT"
    }
  ],
  "route": {
    "rules": [
      {
        "action": "sniff",
        "inbound": "tun-in"
      },
      {
        "action": "hijack-dns",
        "protocol": "dns"
      },
      # {
      #   "action": "route",
      #   "clash_mode": "direct",
      #   "outbound": "DIRECT"
      # },
      # {
      #   "action": "route",
      #   "clash_mode": "global",
      #   "outbound": "GLOBAL"
      # },
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
        "outbound": "DIRECT"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoSite-CN"
        ],
        "outbound": "DIRECT"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoIP-Private"
        ],
        "outbound": "DIRECT"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoIP-CN"
        ],
        "outbound": "DIRECT"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoLocation-!CN"
        ],
        "outbound": "手动选择"
      }
    ],
    "rule_set": [
      {
        "tag": "Category-Ads",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-ads-all.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      },
      {
        "tag": "GeoIP-Private",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/private.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      },
      {
        "tag": "GeoSite-Private",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/private.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      },
      {
        "tag": "GeoIP-CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/cn.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      },
      {
        "tag": "GeoSite-CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/cn.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      },
      {
        "tag": "GeoLocation-!CN",
        "type": "remote",
        "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/geolocation-!cn.srs",
        "format": "binary",
        "download_detour": "DIRECT"
      }
    ],
    "auto_detect_interface": True,
    "final": "手动选择"
  },
  "dns": {
    "servers": [
      {
        "tag": "Local-DNS",
        "address": "https://223.5.5.5/dns-query",
        "address_resolver": "Local-DNS-Resolver",
        "detour": "DIRECT"
      },
      {
        "tag": "Local-DNS-Resolver",
        "address": "223.5.5.5",
        "detour": "DIRECT"
      },
      {
        "tag": "Remote-DNS",
        "address": "tls://8.8.8.8",
        "address_resolver": "Remote-DNS-Resolver",
        "detour": "手动选择"
      },
      {
        "tag": "Remote-DNS-Resolver",
        "address": "8.8.8.8",
        "detour": "手动选择"
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