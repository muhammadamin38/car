a = input("mashina ismini tanlang:")
 
car = {
     "bmw":"2016 yilda yetakchi nemis avtokonsernlaridan biri, BMW (nem. Bayerische Motoren Werke-Bavariya motor zavodi) ozining yuz yilligini nishonlamoqda.Aytish joizki, bu eng birinchi avtomobil zavodi emas, Mercedes-Benz, Opel, Ford, Renault va Fiat kompaniyalari undan avval paydo bolgan, ammo BMW oz sinfining yonalishini belgilab beruvchi avtomobillarni koplab ishlab chiqara olgan, desak xato bolmaydi.",
     "mers":"Mercedes-Benz 1886-yili asos solingan Tashkilotchilar Karl Bents Gotlib Daymler Vilgelm Maybax Joylashuvi Shtutgart, Germaniya MahsulotiYengil avtomobillar, yuk tashuvchi avtomobillar, avtobuslar, dvigatellar Web sahifasi: mercedes-benz.de",
     "chevrolet":"Bugun.uz nashrining keltirishicha, „Ozavtosanoat“ Bo Anderssonni ozining eng yirik korxonalari — „UzAutoMotors“ va „UzAutoMotors Powertrain“larning bosh direktori etib tayinladi[3].",
     "hyundai":"Chung Ju-Yung (1915–2001) 1947 yilda Hyundai Engineering and Construction Company kompaniyasiga asos solgan. Keyinchalik Hyundai Motor Company 1967 yilda tashkil etilgan va kompaniyaning birinchi modeli Cortina 1968 yilda Ford Motor Company bilan hamkorlikda chiqarilgan. Hyundai o'z avtomobilini ishlab chiqmoqchi bo'lganida, ular 1974 yil fevral oyida Britaniyaning Leylanddagi Ostin Morrisning sobiq boshqaruvchi direktori Jorj Turnbullni yolladilar",
     "LADA":"AvtoVAZ avtomobil ishlab chiqaruvchisi, Fiat va Sovet tashqi savdo bo'limi o'rtasidagi hamkorlik natijasida tashkil etilgan va Volga daryosi bo'yidagi Tolyatti shahrida joylashgan"
}

print("siz kiritga", a ,"mashina")


if a.upper() == "BMW":
    print(car["bmw"])

elif a.upper() == "MERS":
     print(car["mers"])

elif a.upper() == "CHEVROLET":
     print(car["chevrolet"])
elif a.upper() == "HYUNDAI":
     print(car["hyundai"])
elif a.upper() == "LADA":
     print(car["LADA"])

else:
     print("malumot yoq")
