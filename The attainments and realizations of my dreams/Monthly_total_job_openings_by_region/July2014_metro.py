import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5]
position_vacancies = [103968, 42281, 28171+5630+1821, 1903+2806+12377, 16746+1861]

label = ["Greater Taipei", "Taoyuan\nHsinchu\nMiaoli", "Taichung\nChanghua\nNantou",
         "Yunlin\nChiayi\nTainan", "Kaohsiung\nPingtung"]

fig, ax = plt.subplots(figsize=(9, 8))
plt.xticks(region_num, labels=label, rotation=7)
# plt.yticks([0, 250, 300, 350, 400, 450, 500, 550])

plot = ax.bar(region_num, position_vacancies)

for rect in plot:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2., 1.002 * height,
            '%d' % int(height), ha='center', va='bottom')

plt.title("2014/07 the number of job openings in Taiwan by metro")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20140702121714/http://www.104.com.tw:80/jb/category/?cat=2")

plt.ylim(10000, 100000)

plt.show()