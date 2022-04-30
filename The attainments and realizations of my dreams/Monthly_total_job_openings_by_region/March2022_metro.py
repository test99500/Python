import matplotlib.pyplot as plt

region_num = [1, 2, 3, 4, 5]
position_vacancies = [178995, 88885, 76159, 39243, 39416]

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

plt.title("2022/03 the number of job openings in Taiwan by metro")

# plt.ylabel("")
plt.xlabel("Reference: https://web.archive.org/web/20220327070711/https://www.104.com.tw/jb/category/?cat=2")

plt.ylim(35000, 165000)

plt.show()