
import pandas as pd
import os
import requests
import fredapi as fa


def Get_Fred_API_Key():
    with open('fredapikey.txt', 'r') as file:
        key = file.readline().strip()
    return key


def Get_Fred_Series(series, name):
    stem = 'https://api.stlouisfed.org/fred/series'
    fred_str = f'?series_id={series}&api_key={fred_api_key}'
    asset_series = fred.get_series(series)
    df = asset_series.to_frame()
    df.reset_index(inplace=True, drop=False)
    df.rename(columns={'index': 'Date', 0: name}, inplace=True)
    return df


"""
To do dev list:
Get API BOE total assets as frequently as possible
Get API ECB total assets as frequently as possible
Get API PBC total assets as frequently as possible
Use groupby to convert them all to the least frequent of the bunch
Create from these a sum at the same frequency of "World_Money_Supply"
import assets of interest(sp500, housing, bitcoin, etc)
allow user to have start and end dates of interest
plot the asset and the asset in total world money supply
"""

fred_api_key = Get_Fred_API_Key()
fred = fa.Fred(api_key=fred_api_key)

# US FED data is weekly
print('Working US Fed...\n')
series = 'RESPPANWW'
Fed_Assets = Get_Fred_Series(series, 'USFED')
print(Fed_Assets)

# ECB


# PBC


# BOE
# https://www.bankofengland.co.uk/boeapps/database/FromShowColumns.asp?Travel=NIxAZxI3x&FromCategoryList=Yes&NewMeaningId=ACRTOT,ATOTAL,ATOTL,AFCAS&CategId=6&HighlightCatValueDisplay=Assets%20-%20total
#series = RPWB75A
# boe_till_14 = "24 May 0686417
# 31 May 0687174
# 07 Jun 0687482
# 14 Jun 0682549
# 21 Jun 0682156
# 28 Jun 0682185
# 05 Jul 0683016
# 12 Jul 0682409
# 19 Jul 0679883
# 26 Jul 0680985
# 02 Aug 0681526
# 09 Aug 0680059
# 16 Aug 0679513
# 23 Aug 0680860
# 30 Aug 0681867
# 06 Sep 0680898
# 13 Sep 0679514
# 20 Sep 0679593
# 27 Sep 0679942
# 04 Oct 0684488
# 11 Oct 0679049
# 18 Oct 0678184
# 25 Oct 0678791
# 01 Nov 0680264
# 08 Nov 0680110
# 15 Nov 0680371
# 22 Nov 0678729
# 29 Nov 0680280
# 06 Dec 0682346
# 13 Dec 0683548
# 20 Dec 0684831
# 27 Dec 0685593
# 03 Jan 0785214
# 10 Jan 0782957
# 17 Jan 0779839
# 24 Jan 0779313
# 31 Jan 0778257
# 07 Feb 0777808
# 14 Feb 0777075
# 21 Feb 0776991
# 28 Feb 0777638
# 07 Mar 0777747
# 14 Mar 0780763
# 21 Mar 0779539
# 28 Mar 0779633
# 04 Apr 0780386
# 11 Apr 0780479
# 18 Apr 0781088
# 25 Apr 0779550
# 02 May 0779416
# 09 May 0779949
# 16 May 0781369
# 23 May 0779015
# 30 May 0781865
# 06 Jun 0780537
# 13 Jun 0780543
# 20 Jun 0781026
# 27 Jun 0779737
# 04 Jul 0799411
# 11 Jul 0779980
# 18 Jul 0780030
# 25 Jul 0780275
# 01 Aug 0781843
# 08 Aug 0780845
# 15 Aug 0781676
# 22 Aug 0780087
# 29 Aug 0783222
# 05 Sep 0784220
# 12 Sep 0783779
# 19 Sep 0795034
# 26 Sep 0798081
# 03 Oct 0793622
# 10 Oct 0789805
# 17 Oct 0791678
# 24 Oct 0795361
# 31 Oct 0792533
# 07 Nov 0793838
# 14 Nov 0795862
# 21 Nov 0797547
# 28 Nov 0796810
# 05 Dec 0796315
# 12 Dec 0797279
# 19 Dec 07107596
# 24 Dec 07102241
# 26 Dec 07102241
# 02 Jan 08101034
# 09 Jan 08101895
# 16 Jan 0896586
# 23 Jan 08102157
# 30 Jan 0894098
# 06 Feb 0895957
# 13 Feb 0896310
# 20 Feb 0897616
# 27 Feb 0896452
# 05 Mar 08105954
# 12 Mar 0897228
# 19 Mar 08102178
# 26 Mar 0898805
# 02 Apr 08100449
# 09 Apr 0898497
# 16 Apr 0899487
# 23 Apr 0896747
# 30 Apr 0892247
# 07 May 08100916
# 14 May 0895142
# 21 May 0894366
# 28 May 0893029
# 04 Jun 0899994
# 11 Jun 0893223
# 18 Jun 0886949
# 25 Jun 0891837
# 02 Jul 0889949
# 09 Jul 0892391
# 16 Jul 0890891
# 23 Jul 0891925
# 30 Jul 0893978
# 06 Aug 0895574
# 13 Aug 0892592
# 20 Aug 0893428
# 27 Aug 0893234
# 03 Sep 0897746
# 10 Sep 0893175
# 17 Sep 08118031
# 24 Sep 08137685
# 01 Oct 08186592
# 08 Oct 08199198
# 15 Oct 08276747
# 22 Oct 08292467
# 29 Oct 08266396
# 05 Nov 08251070
# 12 Nov 08236729
# 19 Nov 08262563
# 26 Nov 08239049
# 03 Dec 08259154
# 10 Dec 08235801
# 17 Dec 08225363
# 24 Dec 08237149
# 31 Dec 08238490
# 07 Jan 09237516
# 14 Jan 09257785
# 21 Jan 09218961
# 28 Jan 09189522
# 04 Feb 09174267
# 11 Feb 09181582
# 18 Feb 09168404
# 25 Feb 09177051
# 04 Mar 09167018
# 11 Mar 09184579
# 18 Mar 09173360
# 25 Mar 09181515
# 01 Apr 09189396
# 08 Apr 09214054
# 15 Apr 09198920
# 22 Apr 09209908
# 29 Apr 09212569
# 06 May 09218178
# 13 May 09215150
# 20 May 09221122
# 27 May 09211324
# 03 Jun 09220596
# 10 Jun 09217030
# 17 Jun 09222718
# 24 Jun 09220105
# 01 Jul 09226582
# 08 Jul 09233730
# 15 Jul 09237695
# 22 Jul 09241789
# 29 Jul 09245318
# 05 Aug 09246639
# 12 Aug 09217354
# 19 Aug 09220511
# 26 Aug 09220252
# 02 Sep 09221614
# 09 Sep 09221225
# 16 Sep 09225989
# 23 Sep 09222713
# 30 Sep 09226407
# 07 Oct 09222200
# 14 Oct 09225173
# 21 Oct 09229966
# 28 Oct 09235345
# 04 Nov 09236942
# 11 Nov 09233543
# 18 Nov 09235221
# 25 Nov 09234631
# 02 Dec 09239261
# 09 Dec 09238787
# 16 Dec 09240431
# 23 Dec 09237966
# 30 Dec 09237694
# 06 Jan 10237756
# 13 Jan 10241940
# 20 Jan 10245484
# 27 Jan 10249695
# 03 Feb 10250690
# 10 Feb 10245950
# 17 Feb 10247280
# 24 Feb 10247966
# 03 Mar 10248275
# 10 Mar 10250553
# 17 Mar 10249470
# 24 Mar 10251621
# 31 Mar 10252336
# 07 Apr 10251670
# 14 Apr 10250312
# 21 Apr 10250180
# 28 Apr 10249906
# 05 May 10249541
# 12 May 10249927
# 19 May 10251165
# 26 May 10252302
# 02 Jun 10252010
# 09 Jun 10251255
# 16 Jun 10250655
# 23 Jun 10251394
# 30 Jun 10250671
# 07 Jul 10250181
# 14 Jul 10249861
# 21 Jul 10251917
# 28 Jul 10252152
# 04 Aug 10251463
# 11 Aug 10250960
# 18 Aug 10249917
# 25 Aug 10247709
# 01 Sep 10247462
# 08 Sep 10247935
# 15 Sep 10245500
# 22 Sep 10244657
# 29 Sep 10244854
# 06 Oct 10244458
# 13 Oct 10243745
# 20 Oct 10243985
# 27 Oct 10244163
# 03 Nov 10244365
# 10 Nov 10244167
# 17 Nov 10242672
# 24 Nov 10245793
# 01 Dec 10245366
# 08 Dec 10245619
# 15 Dec 10246304
# 22 Dec 10247086
# 29 Dec 10246906
# 05 Jan 11246545
# 12 Jan 11244961
# 19 Jan 11242903
# 26 Jan 11241619
# 02 Feb 11241131
# 09 Feb 11241891
# 16 Feb 11241642
# 23 Feb 11240835
# 02 Mar 11245070
# 09 Mar 11244526
# 16 Mar 11242580
# 23 Mar 11242592
# 30 Mar 11242484
# 06 Apr 11242189
# 13 Apr 11241573
# 20 Apr 11240529
# 27 Apr 11240221
# 04 May 11240123
# 11 May 11240210
# 18 May 11239889
# 25 May 11239608
# 01 Jun 11239390
# 08 Jun 11239396
# 15 Jun 11239202
# 22 Jun 11236552
# 29 Jun 11236159
# 06 Jul 11236330
# 13 Jul 11235114
# 20 Jul 11237220
# 27 Jul 11237843
# 03 Aug 11238254
# 10 Aug 11239878
# 17 Aug 11239904
# 24 Aug 11239981
# 31 Aug 11240199
# 07 Sep 11241773
# 14 Sep 11241557
# 21 Sep 11243824
# 28 Sep 11243044
# 05 Oct 11242597
# 12 Oct 11245817
# 19 Oct 11250712
# 26 Oct 11256207
# 02 Nov 11261148
# 09 Nov 11266972
# 16 Nov 11272689
# 23 Nov 11276556
# 30 Nov 11281859
# 07 Dec 11285580
# 14 Dec 11290851
# 21 Dec 11290062
# 28 Dec 11290246
# 04 Jan 12292222
# 11 Jan 12297146
# 18 Jan 12296927
# 25 Jan 12301472
# 01 Feb 12306428
# 08 Feb 12308344
# 15 Feb 12311459
# 22 Feb 12313518
# 29 Feb 12321228
# 07 Mar 12324565
# 14 Mar 12329620
# 21 Mar 12331625
# 28 Mar 12334150
# 04 Apr 12338303
# 11 Apr 12341042
# 18 Apr 12345930
# 25 Apr 12351251
# 02 May 12355451
# 09 May 12356368
# 16 May 12356806
# 23 May 12356252
# 30 May 12356177
# 06 Jun 12356319
# 13 Jun 12355610
# 20 Jun 12355316
# 27 Jun 12360367
# 04 Jul 12360450
# 11 Jul 12362721
# 18 Jul 12365522
# 25 Jul 12372565
# 01 Aug 12375949
# 08 Aug 12378346
# 15 Aug 12381014
# 22 Aug 12384990
# 29 Aug 12386729
# 05 Sep 12390996
# 12 Sep 12393093
# 19 Sep 12396239
# 26 Sep 12399508
# 03 Oct 12402087
# 10 Oct 12404623
# 17 Oct 12407839
# 24 Oct 12411001
# 31 Oct 12413868
# 07 Nov 12414472
# 14 Nov 12414455
# 21 Nov 12414343
# 28 Nov 12414839
# 05 Dec 12414552
# 12 Dec 12415099
# 19 Dec 12414611
# 26 Dec 12410381
# 02 Jan 13410223
# 09 Jan 13409852
# 16 Jan 13409853
# 23 Jan 13405346
# 30 Jan 13404517
# 06 Feb 13404410
# 13 Feb 13404054
# 20 Feb 13404228
# 27 Feb 13402431
# 06 Mar 13402819
# 13 Mar 13405567
# 20 Mar 13403680
# 27 Mar 13404061
# 03 Apr 13403797
# 10 Apr 13403969
# 17 Apr 13404071
# 24 Apr 13403858
# 01 May 13403381
# 08 May 13402968
# 15 May 13402779
# 22 May 13404294
# 29 May 13403771
# 05 Jun 13403404
# 12 Jun 13403386
# 19 Jun 13404220
# 26 Jun 13404092
# 03 Jul 13403852
# 10 Jul 13403965
# 17 Jul 13403789
# 24 Jul 13404055
# 31 Jul 13404889
# 07 Aug 13404995
# 14 Aug 13404566
# 21 Aug 13404377
# 28 Aug 13404591
# 04 Sep 13403987
# 11 Sep 13402949
# 18 Sep 13403261
# 25 Sep 13402990
# 02 Oct 13402275
# 09 Oct 13403246
# 16 Oct 13403215
# 23 Oct 13402950
# 30 Oct 13403291
# 06 Nov 13404340
# 13 Nov 13404868
# 20 Nov 13404272
# 27 Nov 13403430
# 04 Dec 13401973
# 11 Dec 13401388
# 18 Dec 13401479
# 25 Dec 13401729
# 01 Jan 14401261
# 08 Jan 14401472
# 15 Jan 14401622
# 22 Jan 14401867
# 29 Jan 14402280
# 05 Feb 14402814
# 12 Feb 14402162
# 19 Feb 14403089
# 26 Feb 14403617
# 05 Mar 14403709
# 12 Mar 14405312
# 19 Mar 14404304
# 26 Mar 14403786
# 02 Apr 14404026
# 09 Apr 14403888
# 16 Apr 14403722
# 23 Apr 14403335
# 30 Apr 14403613
# 07 May 14403409
# 14 May 14402786
# 21 May 14403174
# 28 May 14403425
# 04 Jun 14403179
# 11 Jun 14403371
# 18 Jun 14404280
# 25 Jun 14404797
# 02 Jul 14404588
# 09 Jul 14404964
# 16 Jul 14404806
# 23 Jul 14404980
# 30 Jul 14404971
# 06 Aug 14405170
# 13 Aug 14404956
# 20 Aug 14404945
# 27 Aug 14405184
# 03 Sep 14405455
# 10 Sep 14404953
# 17 Sep 14404299
# 24 Sep 14405132"
months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
          'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
boe_till_14 = pd.read_csv('boe_till_14.csv', sep=' ', names=['Day', 'Mon', 'Yr+data'])
boe_till_14['Yr+data'] = boe_till_14['Yr+data'].astype(int)
boe_till_14['Yr+data'] = boe_till_14['Yr+data'].astype(str)
boe_till_14['Yr'] = boe_till_14['Yr+data'].str[0:2]
boe_till_14['BOE'] = boe_till_14['Yr+data'].str[2:]
boe_till_14.drop('Yr+data', inplace=True, axis=1)
for idx, row in boe_till_14.iterrows():
    yr = int(boe_till_14.loc[idx, 'Yr'])
    if yr > 14:
        year = '19'+str(yr)
    else:
        year = '20'+str(yr)
    boe_till_14.loc[idx, 'Year'] = year
    day = str(boe_till_14.loc[idx, 'Day'])
    if len(day) == 1:
        day = '0'+day
    mon = str(boe_till_14.loc[idx, 'Mon'])
    mon = months.get(mon)
    boe_till_14.loc[idx, 'Year'] = f'{year}-{mon}-{day}'
boe_till_14.drop(['Day', 'Mon', 'Yr'], axis=1, inplace=True)
boe_till_14.rename(columns={'Year': 'Date'}, inplace=True)
boe_till_14 = boe_till_14[['Date', 'BOE']]
print(boe_till_14)

#

#
