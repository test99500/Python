import matplotlib.pyplot as plt

year = ["2010", "'11", "'12", "'13", "'14", "'15", "'16", "'17", "'18", "'19", "'20", "'21/08", "'21/09"]

northTW = [(3897367 + 2618772 + 460486 + 2002060 + 513015 + 384134 + 415344), # 2010
           (3916451 + 2650968 + 459061 + 2013305 + 517641 + 379927 + 420052), # 2011
           (3939305 + 2673226 + 458595 + 2030161 + 523993 + 377153 + 425071), # 2012
           (3954929 + 2686516 + 458456 + 2044023 + 530486 + 374914 + 428483), # 2013
           (3966818 + 2702315 + 458777 + 2058328 + 537630 + 373077 + 431988), # 2014
           (3970644 + 2704810 + 458117 + 2105780 + 542042 + 372105 + 434060), # 2015
           (3979208 + 2695704 + 457538 + 2147763 + 547481 + 372100 + 437337), # 2016
           (3986689 + 2683257 + 456607 + 2188017 + 552169 + 371458 + 441132), # 2017
           (3995717 + 2668572 + 455221 + 2220872 + 557010 + 370155 + 445635), # 2018
           (4018696 + 2645041 + 454178 + 2249037 + 563933 + 368893 + 448803), # 2019
           (4030954 + 2602418 + 453087 + 2268807 + 570775 + 367577 + 451412), # 2020
           #           (4019898 + 2553798 + 451635 + 2272976 + 573858 + 365591 + 452781), # 2021/08
           #           (4017632 + 2544720 + 451422 + 2272812 + 574512 + 365117 + 452882), # 2021/09
           (4011586 + 2531659 + 450944 + 2272452 + 575131 + 364350 + 452665), # 2021/11
           ]

centralTW = [(2648419 + 560968 + 1307286 + 526491 + 717653), # 2010
             (2664394 + 562010 + 1303039 + 522807 + 713556), # 2011
             (2684893 + 563976 + 1299868 + 520196 + 710991), # 2012
             (2701661 + 565554 + 1296013 + 517222 + 707792), # 2013
             (2719835 + 567132 + 1291474 + 514315 + 705356), # 2014
             (2744445 + 563912 + 1289072 + 509490 + 699633), # 2015
             (2767239 + 559189 + 1287146 + 505163 + 694873), # 2016
             (2787070 + 553807 + 1282458 + 501051 + 690373), # 2017
             (2803894 + 548863 + 1277824 + 497031 + 686022), # 2018
             (2815261 + 545459 + 1272802 + 494112 + 681306), # 2019
             (2820787 + 542590 + 1266670 + 490832 + 676873), # 2020
             #             (2818139 + 539879 + 1259246 + 487185 + 672557), # 2021/08
             #             (2816393 + 539361 + 1257991 + 486455 + 671686), # 2021/09
             (2814422 + 538568 + 1256062 + 485479 + 670664), # 2021/11
             ]

southTW = [(1873794 + 2773483 + 543248 + 873509 + 272390), # 2010
           (1876960 + 2774470 + 537942 + 864529 + 271526), # 2011
           (1881645 + 2778659 + 533723 + 858441 + 271220), # 2012
           (1883208 + 2779877 + 529229 + 852286 + 270872), # 2013
           (1884284 + 2778992 + 524783 + 847917 + 270883), # 2014
           (1885541 + 2778918 + 519839 + 841253 + 270366), # 2015
           (1886033 + 2779371 + 515320 + 835792 + 269874), # 2016
           (1886522 + 2776912 + 511182 + 829939 + 269398), # 2017
           (1883831 + 2773533 + 507068 + 825406 + 268622), # 2018
           (1880906 + 2773198 + 503113 + 819184 + 267690), # 2019
           (1874917 + 2765932 + 499481 + 812658 + 266005), # 2020
           #           (1867554 + 2753530 + 495662 + 807159 + 264858), # 2021/08
           #           (1866073 + 2751317 + 494868 + 806305 + 265002), # 2021/09
           (1863435 + 2746939 + 493855 + 805177 + 264954), # 2021/11
           ]

eastTW = [(338805 + 230673), # 2010
          (336838 + 228290), # 2011
          (335190 + 226252), # 2012
          (333897 + 224821), # 2013
          (333392 + 224470), # 2014
          (331945 + 222452), # 2015
          (330911 + 220802), # 2016
          (329237 + 219540), # 2017
          (327968 + 218919), # 2018
          (326247 + 216781), # 2019
          (324372 + 215261), # 2020
          #          (322506 + 213956), # 2021/08
          #          (322260 + 213818), # 2021/09
          (321697 + 213534), # 2021/11
          ]

outlyingTW = [(107308 + 96918), # 2010 Fujian + Penghu
              (113989 + 97157), # 2011
              (124421 + 98843), # 2012
              (132878 + 100400), # 2013
              (140229 + 101758), # 2014
              (145346 + 102304), # 2015
              (147709 + 103263), # 2016
              (150336 + 104073), # 2017
              (152329 + 104440), # 2018
              (153274 + 105207), # 2019
              (153876 + 105952), # 2020
              #              (140004 + 13420 + 105645), # 2021/08
              #              (140856 + 13429 + 106036), # 2021/09
              (141327 + 13577 + 106310), # 2021/11
              ]

x = range(10, 22)

date = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
index = [(330.60 + 129.45) / 2]
housing_index = [(91.03 + 191.07) / 2, # 2010/04 (Guotai index + Xinyi index) / 2
                 (102.42 + 218.72) / 2, # 2011/04
                 (109.85 + 241.27) / 2, # 2012/04
                 (117.29 + 278.51) / 2, # 2013/04
                 (124.60 + 297.78) / 2, # 2014/04
                 (124.61 + 289.3) / 2,  # 2015/04
                 (95.92 + 279.74) / 2, # 2016/04
                 (101.89 + 282.36) / 2, # 2017/04
                 (107.48 + 285.55) / 2, # 2018/04
                 (114.48 + 294.46) / 2, # 2019/04
                 (125.22 + 302.61) / 2, # 2020/04
                 #                 (129.45 + 333.60) / 2, # 2021/04
                 (134.69 + 341.62) / 2,  # 2021/07
                 (128.33 + )
                 ]

figure, axes = plt.subplots()

axes.stackplot(x, northTW, centralTW, southTW, eastTW, outlyingTW, labels=year)
axes.set_ylim(23350000, 23700000)
axes.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
axes.set_xlabel("Year\n"
                "References:\n"
                "1. https://www.ris.gov.tw/app/portal/346 \n"
                "2. https://www.macromicro.me/collections/15/\n"
                "tw-housing-relative/124/tw-housing-price-sinyi")

axes.set_ylabel("Population (Unit: 10 millions)")

axes2 = axes.twinx()
axes2.set_ylabel("Yearly Housing Price Index (2010/04 - 2021/07) \n"
                 "Method: (Guotai + Xinyi) / 2", color='goldenrod')

axes2.plot(x, housing_index, color='gold')
axes2.tick_params(axis='y', labelcolor='goldenrod')

plt.grid(linewidth=0.3)
plt.title("Taiwan's population change from 2010 - 2021/11 \n in relation to Annual Housing Price Index")

figure.tight_layout()

plt.show()

# References:
# 1. https://pip.moi.gov.tw/V3/E/SCRE0201.aspx
# 2. https://www.cathay-red.com.tw/tw/About/House
# 3. https://www.sinyinews.com.tw/quarterly
