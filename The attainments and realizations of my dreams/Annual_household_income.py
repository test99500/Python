import matplotlib.pyplot as plt

year = [2015, 2016, 2017, 2018, 2019, 2020]
income_Kaohsiung = [1145895, 1166824, 1186204, 1219246, 1224268, 1224100]
income_Tainan = [1007093, 1063495, 1079199, 1086077, 1079174, 1086475]
income_Taichung = [1169183, 1140325, 1245350, 1279865, 1298497, 1289700]
income_Taoyuan = [1307158, 1317790, 1337361, 1378732, 1392199, 1424027]
income_Taipei = [1581899, 1568945, 1648122, 1649348, 1723021, 1716591]
income_New_Taipei = [1171978, 1223867, 1265798, 1292753, 1319841, 1352548]
income_Hsinchu_county = [1283995, 1365150, 1616327, 1519478, 1539555, 1619782]
income_Hsinchu_city = [1427572, 1537317, 1572296, 1426379, 1602826, 1618903]
income_Miaoli_county = [1008241, 1166196, 1029485, 1045881, 1073028, 1161999]

plt.plot(year, income_Taipei, label="Taipei")
plt.plot(year, income_New_Taipei, label="New Taipei")
plt.plot(year, income_Taoyuan, label="Taoyuan")
plt.plot(year, income_Hsinchu_county, label="Hsinchu county")
plt.plot(year, income_Hsinchu_city, label="Hsinchu city")
plt.plot(year, income_Miaoli_county, label="Miaoli")
plt.plot(year, income_Taichung, label="Taichung")
plt.plot(year, income_Tainan, label="Tainan")
plt.plot(year, income_Kaohsiung, label="Kaohsiung")

plt.title("Annual household income by region in Taiwan")
plt.legend()
plt.grid(linewidth=0.7)
plt.ylabel("Income (1 million New Taiwan Dollar)")

plt.savefig("Annual_household_income")
plt.show()
