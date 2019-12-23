import requests

# 四台接口服务器
ips = ["172.18.56.27:8884", "172.18.56.28:8884", "172.18.56.29:8884", "172.18.56.30:8884"]
interfaces = ["refreshMsgNumberOrgCache", "refreshMenuCache", "refreshCardCache", "refreshRuleCache"]
paths = "/api/reload/"


# 刷新机构号码和logo 缓存
def clear_institution_cache():
    n = 0
    for i in ips:
        url = "http://" + i + paths + interfaces[0]
        response = requests.get(url, timeout=10)
        n += 1
        if response.status_code == 200:
            print("第%s台服务器机构和logo信息缓存清除成功..." % n)
        else:
            print("第%s台服务器机构和logo信息缓存清除失败..." % n)


# 刷新菜单缓存
def clear_menu_cache():
    n = 0
    for i in ips:
        url = "http://" + i + paths + interfaces[1]
        response = requests.get(url, timeout=10)
        n += 1
        if response.status_code == 200:
            print("第%s台服务器菜单信息缓存清除成功..." % n)
        else:
            print("第%s台服务器菜单信息缓存清除失败..." % n)


# 刷新卡片缓存
def clear_card_cache():
    n = 0
    for i in ips:
        url = "http://" + i + paths + interfaces[2]
        response = requests.get(url, timeout=10)
        n += 1
        if response.status_code == 200:
            print("第%s台服务器卡片信息缓存清除成功..." % n)
        else:
            print("第%s台服务器卡片信息缓存清除失败..." % n)


# 刷新js 规则缓存
def clear_js_cache():
    n = 0
    for i in ips:
        url = "http://" + i + paths + interfaces[3]
        response = requests.get(url, timeout=10)
        n += 1
        if response.status_code == 200:
            print("第%s台服务器JS信息缓存清除成功..." % n)
        else:
            print("第%s台服务器JS信息缓存清除失败..." % n)


if __name__ == "__main__":
    clear_institution_cache()
    clear_menu_cache()
    clear_card_cache()
    clear_js_cache()


