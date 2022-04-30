import matplotlib.pyplot as plt
import matplotlib
# Using the magic encoding
# -*- coding: utf-8 -*-

matplotlib.rc('font', family="MS Gothic")

region_num = [1, 2, 3, 4, 5]
position_vacancies = [179197, 89380, 76630, 39687, 40032]

label = ["大台北", "桃園\n新竹\n苗栗", "台中T\n彰化\n南投",
         "雲林\n嘉義\n台南", "高雄\n屏東"]

fig, ax = plt.subplots(figsize=(9, 8))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2022/04 台灣各生活圈職缺數統計\n the number of job openings in Taiwan by metro", fontproperties="MS Gothic")

# plt.ylabel("")
plt.xlabel("參考資料: https://web.archive.org/web/20220428163845/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(35000, 165000)

plt.show()
