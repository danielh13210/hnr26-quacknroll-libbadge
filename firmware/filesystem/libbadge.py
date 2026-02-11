from lib.libbadge.main import Hardware

__hw=Hardware()
def __getattr__(attr):
    return getattr(__hw,attr)