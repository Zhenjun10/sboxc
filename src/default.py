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
      "external_controller": "127.0.0.1:20123",
      "external_ui": "",
      "external_ui_download_url": "",
      "external_ui_download_detour": "DIRECT",
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
        "192.168.255.252/30"
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
    },
    {
      "type": "selector",
      "tag": "GLOBAL",
      "interrupt_exist_connections": True,
      "outbounds": [
        "自动选择",
        "手动选择"
      ]
    },
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
      {
        "action": "route",
        "clash_mode": "direct",
        "outbound": "DIRECT"
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
    "final": "手动选择",
    "default_domain_resolver": {
      "server": "Local-DNS"
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
    "rules": [
      {
        "action": "route",
        "clash_mode": "direct",
        "server": "Local-DNS"
      },
      {
        "action": "route",
        "clash_mode": "global",
        "server": "Remote-DNS"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoSite-CN"
        ],
        "server": "Local-DNS"
      },
      {
        "action": "route",
        "rule_set": [
          "GeoLocation-!CN"
        ],
        "server": "Remote-DNS"
      }
    ],
    "disable_cache": False,
    "disable_expire": False,
    "independent_cache": False,
    "final": "Remote-DNS"
  }
}