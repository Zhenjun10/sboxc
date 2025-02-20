class Configer:
    def __init__(self) -> None:
        self.config = {
        # 配置文件参考资料 https://sing-box.sagernet.org/zh/configuration/
            "log": {
                "disabled": False,
                "level": "info",  # 日志等级，可选值：trace debug info warn error fatal panic
                # "output": "sing-box.log",  # 输出文件路径，启动后将不输出到控制台
                "timestamp": True  # 添加时间到每行
            },
            "dns": {
                "servers": [
                    {
                        "tag": "GoogleDNS",  # DNS 服务器的标签
                        "address": "tls://8.8.8.8",  # DNS 服务器的地址
                        "address_resolver": "8.8.8.8",  # 如果服务器地址包括域名则必须，用于解析本 DNS 服务器的域名的另一个 DNS 服务器的标签
                        # 用于解析本 DNS 服务器的域名的策略。
                        # 可选项：prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only。默认使用 dns.strategy
                        "address_strategy": "",
                        "strategy": "",  # 默认解析策略。可选项：prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only。如果被其他设置覆盖则不生效
                        "detour": "GLOBAL",  # 用于连接到 DNS 服务器的出站的标签。如果为空，将使用默认出站
                        "client_subnet": "202.103.44.150"
                    },
                    {
                        "tag": "LocalDNS",  # DNS 服务器的标签
                        "address": "https://223.5.5.5/dns-query",  # DNS 服务器的地址
                        "address_resolver": "223.5.5.5",  # 如果服务器地址包括域名则必须，用于解析本 DNS 服务器的域名的另一个 DNS 服务器的标签
                        # 用于解析本 DNS 服务器的域名的策略。
                        # 可选项：prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only。默认使用 dns.strategy
                        "address_strategy": "",
                        "strategy": "",  # 默认解析策略。可选项：prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only。如果被其他设置覆盖则不生效
                        "detour": "DIRECT",  # 用于连接到 DNS 服务器的出站的标签。如果为空，将使用默认出站
                        "client_subnet": ""
                    },
                ],
                "rules": [
                    {
                        "clash_mode": "Direct",  # 匹配 Clash 模式
                        "server": "LocalDNS"  # 必填，目标 DNS 服务器的标签
                    },
                    {
                        "clash_mode": "Global",
                        "server": "GoogleDNS"
                    },
                    {
                        "rule_set": "DirectRules",  # 匹配规则集
                        "server": "LocalDNS"
                    },
                ],
                "final": "GoogleDNS",  # 默认 DNS 服务器的 tag (标签)，默认使用第一个服务器
                # 默认解析域名策略，可选值: prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only
                # 如果设置了 server.strategy，则不生效
                "strategy": "ipv4_only",
                "disable_cache": False,  # 禁用 DNS 缓存
                "disable_expire": False,  # 禁用 DNS 缓存过期
                "independent_cache": False,  # 使每个 DNS 服务器的缓存独立，以满足特殊目的。如果启用，将轻微降低性能
                "reverse_mapping": False,  # 在响应 DNS 查询后存储 IP 地址的反向映射以为路由目的提供域名
                # 默认情况下，将带有指定 IP 前缀的 edns0-subnet OPT 附加记录附加到每个查询
                # 如果值是 IP 地址而不是前缀，则会自动附加 /32 或 /128
                # 可以被 servers.[].client_subnet 或 rules.[].client_subnet 覆盖
                "client_subnet": "",
                "fakeip": {
                    "enabled": False,  # 启用 FakeIP 服务
                    "inet4_range": "198.18.0.0/15",  # 用于 FakeIP 的 IPv4 地址范围
                    "inet6_range": "fc00::/18"
                }
            },
            "inbounds": [  # 入站
                {
                    "type": "mixed",
                    "tag": "mixed-in",

                    # 监听字段
                    "listen": "127.0.0.1",  # 监听地址，必填
                    "listen_port": 20122,  # 监听端口
                    "tcp_fast_open": False,  # 启用 TCP Fast Open
                    "tcp_multi_path": False,  # 启用 TCP Multi Path，需要 Go 1.21
                    "udp_fragment": False,  # 启用 UDP 分段
                    "udp_timeout": "5m",  # UDP NAT 过期时间，以秒为单位。默认使用 5m
                    "detour": "",  # 如果设置，连接将被转发到指定的入站。需要指定的入站，注入支持
                    "sniff": True,  # 启用协议探测
                    "sniff_override_destination": False,  # 用探测出的域名覆盖连接目标地址。如果域名无效（如 Tor），将不生效
                    "sniff_timeout": "300ms",  # 探测超时时间。默认使用 300ms
                    # 如果设置，请求的域名将在路由之前解析为 IP
                    # 如果 sniff_override_destination 生效，它的值将作为后备
                    # 可选值： prefer_ipv4 prefer_ipv6 ipv4_only ipv6_only
                    "domain_strategy": "ipv4_only",
                    # 如果启用，对于地址为域的 UDP 代理请求，将在响应中发送原始包地址而不是映射的域。
                    # 此选项用于兼容不支持接收带有域地址的 UDP 包的客户端，如 Surge
                    "udp_disable_domain_unmapping": False,
                    # END

                    # "users": [  # SOCKS 和 HTTP 用户，如果为空则不需要验证
                    #     {
                    #         "username": "admin",
                    #         "password": "admin"
                    #     }
                    # ],

                    # 启动时自动设置系统代理，停止时自动清理
                    # 仅支持 Linux、Android、Windows 和 macOS。
                    # 要在无特权的 Android 和 iOS 上工作，请改用 tun.platform.http_proxy。
                    "set_system_proxy": True
                }
            ],
            "outbounds": [
                {
                    "type": "direct",
                    "tag": "DIRECT",

                    # "override_address": "1.0.0.1",  # 覆盖连接目标地址
                    # "override_port": 53,  # 覆盖连接目标端口
                    # # 写出 代理协议 到连接头。
                    # # 可用协议版本值: 1 或 2
                    # "proxy_protocol": 0,

                    # ...  # 拨号字段
                },
                {
                    "type": "block",
                    "tag": "REJECT"
                },
                {
                    "type": "selector",
                    "tag": "手动选择",

                    "outbounds": [  # 用于选择的出站标签列表，包含 所有出站，除去 自身 与 GLOBAL
                        "DIRECT",
                        "REJECT",
                        "自动选择"
                    ],
                    "default": "自动选择",  # 默认的出站标签。默认使用第一个出站
                    # 当选定的出站发生更改时，中断现有连接。
                    # 仅入站连接受此设置影响，内部连接将始终被中断
                    "interrupt_exist_connections": False
                },
                {
                    "type": "urltest",
                    "tag": "自动选择",

                    "outbounds": [],  # 用于测试的出站标签列表，包含 所有节点
                    "url": "https://www.gstatic.com/generate_204",  # 用于测试的链接。默认使用 https://www.gstatic.com/generate_204
                    "interval": "300s",  # 测试间隔。 默认使用 3m
                    "tolerance": 150,  # 以毫秒为单位的测试容差。 默认使用 50
                    "idle_timeout": "",  # 空闲超时。默认使用 30m
                    "interrupt_exist_connections": False
                },
                {
                    "type": "selector",
                    "tag": "GLOBAL",
                    "outbounds": ["自动选择"],  # 包含 自动选择 和 所有节点
                    "default": "自动选择"
                },
                {
                    "type": "dns",
                    "tag": "DNS"
                }
            ],
            "route": {
                "rules": [
                    {
                        "clash_mode": "Direct",
                        "outbound": "DIRECT"
                    },
                    {
                        "clash_mode": "Global",
                        "outbound": "GLOBAL"
                    },
                    {
                        "rule_set": "DirectRules",
                        "outbound": "DIRECT"
                    },
                    {
                        "rule_set": "ProxyRules",
                        "outbound": "手动选择"
                    },
                    {
                        "rule_set": "RejectRules",
                        "outbound": "REJECT"
                    },
                    {
                        "ip_is_private": True,
                        "outbound": "DIRECT"
                    },
                    {
                        "protocol": "dns",
                        "port": 53,
                        "outbound": "DNS"
                    },
                    {
                        "network": "udp",  # 拦截 443 端口的 UDP 网络?
                        "port": 443,
                        "outbound": "REJECT"
                    },
                ],
                "rule_set": [
                    {
                    "type": "local",  # 必需，有三种，inline, local, remote
                    "tag": "DirectRules",
                    "format": "binary",  # 必需，有两种，source 或者 binary
                    "path": "DirectRules"
                    },
                    {
                    "type": "local",
                    "tag": "ProxyRules",
                    "format": "binary",  # or source
                    "path": "ProxyRules"
                    },
                    {
                    "type": "local",
                    "tag": "RejectRules",
                    "format": "binary",  # or source
                    "path": "RejectRules"
                    }
                ],
                "final": "",  # 默认出站标签。如果为空，将使用第一个可用于对应协议的出站
                # 默认将出站连接绑定到默认网卡，以防止在 tun 下出现路由环路。
                # 如果设置了 outbound.bind_interface 设置，则不生效
                # 仅支持 Linux、Windows 和 macOS
                "auto_detect_interface": True,
                # 启用 auto_detect_interface 时接受 Android VPN 作为上游网卡
                # 仅支持 Android
                "override_android_vpn": False,
                # # 默认将出站连接绑定到指定网卡，以防止在 tun 下出现路由环路。
                # # 如果设置了 auto_detect_interface 设置，则不生效
                # # 仅支持 Linux、Windows 和 macOS
                # "default_interface": "en0",
                # # 默认为出站连接设置路由标记。
                # # 如果设置了 outbound.routing_mark 设置，则不生效
                # # 仅支持 Linux
                # "default_mark": 233
            },
            "experimental": {
                "cache_file": {  # 缓存文件
                    "enabled": True,  # 启用缓存文件
                    "path": "",  # 缓存文件路径，默认使用cache.db
                    # 缓存文件中的标识符
                    # 如果不为空，配置特定的数据将使用由其键控的单独存储。
                    "cache_id": "",
                    "store_fakeip": False,  # 将 fakeip 存储在缓存文件中
                    "store_rdrc": False,  # 将拒绝的 DNS 响应缓存存储在缓存文件中
                    "rdrc_timeout": ""  # 拒绝的 DNS 响应缓存超时，默认使用 7d (7天)
                },
                "clash_api": {
                    "external_controller": "127.0.0.1:9090",  # RESTful web API 监听地址。如果为空，则禁用 Clash API
                    "external_ui": "",  # 到静态网页资源目录的相对路径或绝对路径。sing-box 会在 http://{{external-controller}}/ui 下提供它
                    # 静态网页资源的 ZIP 下载 URL，如果指定的 external_ui 目录为空，将使用默认值
                    # 默认使用 https://github.com/MetaCubeX/Yacd-meta/archive/gh-pages.zip
                    "external_ui_download_url": "",
                    "external_ui_download_detour": "",  # 用于下载静态网页资源的出站的标签。如果为空，将使用默认出站
                    "secret": "",  # RESTful API 的密钥（可选） 通过指定 HTTP 标头 Authorization: Bearer ${secret} 进行身份验证 如果 RESTful API 正在监听 0.0.0.0，请始终设置一个密钥
                    "default_mode": "",  # Clash 中的默认模式，默认使用 Rule。此设置没有直接影响，但可以通过 clash_mode 规则项在路由和 DNS 规则中使用
                    "access_control_allow_origin": [],  # 允许的 CORS 来源，默认使用 *。要从公共网站访问私有网络上的 Clash API，必须在 access_control_allow_origin 中明确指定它而不是使用 *
                    "access_control_allow_private_network": False,  # 允许从私有网络访问。要从公共网站访问私有网络上的 Clash API，必须启用 access_control_allow_private_network
                },
                # "v2ray_api": {}
            }
        }

    def node_convert(self):
        ...

    def add_node(self):
        ...

    def save_config(self, filename: str = None):
        '''保存`config`文件
        :param filename: 文件名，默认为 `config.json`
        :return: 无
        '''
        import json
        if filename is None:
            filename = "config.json"
        json.dump(self.config, open(f"build/{filename}", "w+", encoding="utf-8"), indent=2, ensure_ascii=False)
        # self.log('DONE', "DirectRules and ProxyRules generated")


if __name__ == "__main__":
    config = Configer()
    # config.save_config()
    print(config.config["outbounds"])
