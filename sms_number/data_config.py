class GlobalVar(object):
    """
    配置case 列名
    """
    number = 0
    organization = 1
    business = 2


def get_number():
    return GlobalVar.number


def get_organization():
    return GlobalVar.organization


def get_business():
    return GlobalVar.business

