# @version: 1.12.0
# @author: cheremace

# 配置文件参考资料 https://sing-box.sagernet.org/zh/configuration/
config = {
    "log": {
        "disabled": False,
        # 日志等级，可选值：trace debug info warn error fatal panic
        "level": "info",
        # 输出文件路径，启动后将不输出到控制台
        # "output": "sing-box.log",
        # 添加时间到每行
        "timestamp": True
    },
    "dns": {
        # 一组 DNS 服务器
        "servers": [
            {
                "type": "tls",
                "tag": "GoogleDNS",

                "server": "8.8.8.8",
                "server_port": 853,

                "tls": {
                    "enabled": True,
                    "disable_sni": False,
                    "server_name": "",
                    "insecure": False,
                    "alpn": [],
                    "min_version": "",
                    "max_version": "",
                    "cipher_suites": [],
                    "certificate": "",
                    "certificate_path": "",
                    "fragment": False,
                    "fragment_fallback_delay": "",
                    "record_fragment": False,
                    "ech": {
                        "enabled": False,
                        "config": [],
                        "config_path": "",

                        # Deprecated
                        "pq_signature_schemes_enabled": False,
                        "dynamic_record_sizing_disabled": False
                    },
                    "utls": {
                        "enabled": False,
                        "fingerprint": ""
                    },
                    "reality": {
                        "enabled": False,
                        "public_key": "jNXHt1yRo0vDuchQlIP6Z0ZvjT3KtzVI-T4E7RoLJS0",
                        "short_id": "0123456789abcdef"
                    }
                },
            }
        ],
        # 一组 DNS 规则
        "rules": [],
        # 默认 DNS 服务器的 tag (标签)，默认使用第一个服务器
        "final": "GoogleDNS",
        # 默认解析域名策略
        "strategy": "ipv4_only",
        # 禁用 DNS 缓存
        "disable_cache": False,
        # 禁用 DNS 缓存过期
        "disable_expire": False,
        # 使每个 DNS 服务器的缓存独立，以满足特殊目的。如果启用，将轻微降低性能
        "independent_cache": False,
        # LRU 缓存容量
        "cache_capacity": 0,
        "reverse_mapping": False,
        "client_subnet": "",
        "fakeip": {
            "enabled": False,  # 启用 FakeIP 服务
            "inet4_range": "198.18.0.0/15",  # 用于 FakeIP 的 IPv4 地址范围
            "inet6_range": "fc00::/18"
        }
    },
    "ntp": {},
    "certificate": {},
    "endpoints": [],
    "inbounds": [],
    "outbounds": [],
    "route": {},
    "experimental": {}
}