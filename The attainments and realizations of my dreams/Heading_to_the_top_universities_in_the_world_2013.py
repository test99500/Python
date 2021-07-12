import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
# Using the magic encoding
# -*- coding: utf-8 -*-


# Convert wiki-table in the article 高等教育深耕計畫[4] to csv.[2][3]

university = pd.DataFrame(data=[
    [1, "國立臺灣大學", "National Taiwan University", 310000, "North", ],
    [2, "國立成功大學", "National Cheng Kung University", 160000, "South", ],
    [3, "國立清華大學", "National Tsing Hua University", 120000, "North", "Derived from Beijing, China's Tsing Hua University"],
    [4, "國立交通大學", "National Chiao Tung University", 100000, "North", "Derived from Shanghai, China's ChiaoTung University"],
    [5, "國立中央大學", "National Central University", 70000, "North", ],
    [7, "國立陽明大學", "National Yang Ming University", 50000, "North", ],
    [6, "國立中山大學", "National Sun Yat-sen University", 40000, "South", "Derived from Guangzou, China's Sun Yat-sen University"],
    [8, "國立中興大學", "National Chung Hsing University", 30000, "North", ],
    [9, "長庚大學", "Chang Gung University", 20000, "North"],
    [10, "國立政治大學", "National Chengchi University", 20000, "North", "Literally, 'National Politics University'"],
    [11, "國立臺灣科技大學", "National Taiwan University of Science and Technology", 20000, "North"],
    [12, "國立臺灣師範大學", "National Taiwan Normal University", 20000, "North", ],
    [13, "國立臺灣海洋大學", "National Taiwan Ocean University", 10000, "North", ],
    [14, "國立中正大學", "National Chung Cheng University", 10000, "South", "Literally, National Chiang Chung-cheng University"],
])

print(university)

header = ['Number', 'Chinese name', 'English name', 'Budget_received', 'Location', 'Note']

# Adding a header to universities of R&D
university.columns = header
print(university)

# Filter the universities in the north.
condition = university['Location'] == 'North'
north_university = university[condition]
print(north_university)

# Sum of the budget in the north.
total_north_university = north_university['Budget_received'].sum()
print(total_north_university)

# Filter the universities in the south.
condition = university['Location'] == 'South'
south_university = university[condition]
print(south_university)

# Sum of the budget in the south.
total_south_university = south_university['Budget_received'].sum()
print(total_south_university)

# The histogram of the data
plt.bar(['Northern Taiwan', 'Southern Taiwan'], [total_north_university, total_south_university])

plt.xlabel('Location (divided by Zhushui river)\n'
           'Dataset:\nhttps://web.archive.org/web/20210615094117/'
           'https://zh.wikipedia.org/wiki/邁向頂尖大學計畫',
           fontproperties="MS Gothic", fontsize=9) #[1]

plt.ylabel('Unit: 10 thousands of New Taiwan Dollars')

plt.title('Government budget support for\n'
          'research-centric universities\n'
          'in North vs South in 2013', fontproperties="Arial")

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

plt.savefig('Total_difference_2013.jpg')
plt.show()

university.to_excel("Heading_to_the_top_universities_in_the_world_2013.xlsx")

# References:
# 1. https://stackoverflow.com/a/12444777/14900011
