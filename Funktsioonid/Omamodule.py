def pikkus(ikood:int)->bool:
    """Funktsioon tagastab True, kui pikkus on 11 sümbolid
    :param str ikood: Inimese isikukood
    :rtype: bool
    """
    if len(ikood)==11:
        flag=True
    else:
        flag=False
    return flag
    
def sugu(ikood:str)->str:
    """Kui esimene täht on [1,2,3,4,5,6], siis määrame sugu
    :param str ikood:
    :rtype: str
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s

def sunnipaev(ikood:str):
    ikood_list=list(map(int,ikood))
    y=str(ikood_list[1])+str(ikood_list[2])
    m=str(ikood_list[3])+str(ikood_list[4])
    d=str(ikood_list[5])+str(ikood_list[6])

    if int(m)>0 and int(m)<13 and int(d)>0 and int(d)<32:
        if ikood_list[0] in [1,2]:
            yy="18"
        elif ikood_list[0] in [3,4]:
            yy="19"
        else:
            yy="20"
        spaev=d+"."+m+"."+yy+y
    else:
        spaev="viga"
    return spaev

def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood_list[7]+ikood_list[8]+ikood_list[9]
    t=int(tahed_8910)
    if 1<t<10:
        haigla="Kuressare Haigla"
    elif 11>t>19:
        haigla="Ida-Tallina"
    elif 221<t<270:
        haigla="Ida_Viru Keskhaigla"
    else:
        haigla="Välismaal"
    return haigla

def lause()->str:
    print(f"see on {sugu(ikood)} ta on sündinud {sunnipaev(ikood)}, tema sünnikoht on {sunnikoht(ikood)}")

