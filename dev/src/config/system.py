import os, sys


reload(sys)
sys.setdefaultencoding("utf-8")

dir_name = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_name, "..", "..", "..", "dep", "lib"))
sys.path.append(os.path.join(dir_name, "..", "..", "..", "dep", "lib", "WxPay"))


sys.path.append(os.path.join(dir_name, "..", "..", "..", "dep"))

