import random

def matin(ha_mon,i):  #ha_monが所持金,iが所持金の何倍になったら終了するか
    goal=ha_mon*i  #初期のha_monの2倍
    jijou=1 #かけるお金
    while(ha_mon>1):    #所持金が0円になったら終了
        if(ha_mon<jijou):
            print("賭けるお金が",jijou,"円で所持金が",ha_mon,"円のため賭けは終了です")
            break
        ha_mon=ha_mon-jijou #お金をかける
        num=random.randint(0, 99)   #ランダムな数字
        if(num%2==0):
            ha_mon=ha_mon+jijou*2   #当たればお金がもらえる
            jijou=1 #賭け金を1にする
            print("出力されたランダムの数字",num,"\t所持金",ha_mon)
        else:
            jijou=jijou*2   #外れたら賭け金を2倍にする
            print("出力されたランダムの数字",num,"\t所持金",ha_mon)
        if(ha_mon==goal):    #所持金がha_monのi倍になったら終了
            break
        
matin(1000,2)  #(所持金,所持金の何倍になったら終了するか)