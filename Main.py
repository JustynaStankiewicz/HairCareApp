import Zarzadzanie
from Wlosy import Wlosy

if __name__ == '__main__':
    wlosy=Wlosy()
    zarzadzanie=Zarzadzanie.Zarzadzanie(wlosy)
    zarzadzanie.panel_wyboru_funkcji()