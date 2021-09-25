import matplotlib.pyplot as plt

year = ["2010", "'11", "'12", "'13", "'14", "'15", "'16", "'17", "'18", "'19", "'20", "'21/08"]

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
           (4019898 + 2553798 + 451635 + 2272976 + 573858 + 365591 + 452781), # 2021/08
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
             (2818139 + 539879 + 1259246 + 487185 + 672557), # 2021/08
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
           (1867554 + 2753530 + 495662 + 807159 + 264858), # 2021/08
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
          (322506 + 213956), # 2021/08
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
              (140004 + 13420 + 105645) # 2021/08
              ]

x = range(10, 22)

figure, axes = plt.subplots()

axes.stackplot(x, northTW, centralTW, southTW, eastTW, outlyingTW, labels=year)
plt.ylim(23000000, 23700000)

plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

plt.grid(linewidth=0.3)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Taiwan's population change from 2010 - 2021/08 ")

plt.show()
