import requests
import urllib
import urllib.request
import re
import os
import shutil


def File_Checker():  # Check if output files exist or not

    if(os.path.exists('steam_sale.html')):
        os.remove('steam_sale.html')  # Check html file


# STEAM_SPIDER
def Steam_Spider():

    page = 0  # This loop may not suit this site, use when necessary
    while(page < 1):

        url = 'https://store.steampowered.com/specials#p=' + \
            str(page) + '&tab=TopSellers'  # Sale page

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        r = requests.get(url)
        r = requests.get(url, headers=header)

        content = r.text

        f = open('steam_sale.html', 'a', encoding=r.encoding, errors='ignore')
        print(r.text, file=f)

        f.close()
        print('Completed with ' + r.encoding)  # Site 's HTML encoding
        page = page + 1


def getNonRepeatList(data):  # No-repeat tool
    return [i for n, i in enumerate(data) if i not in data[:n]]


def Output():
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # yellow
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple

    discount_img = []
    discount_name = []
    discount_original_price = []
    discount_pct = []
    discount_final_price = []
    with open('steam_sale.html', 'r', encoding='UTF-8', errors='ignore') as f2:
        line = f2.readline()
        list1 = []

        while line:

            try:
                line = f2.readline()

                if 'tab_item_name' in line:
                    print(re.findall(
                        r'<div\sclass="tab_item_name">(.+?)</div>', line)[0])
                    discount_name.append(re.findall(
                        r'<div\sclass="tab_item_name">(.+?)</div>', line)[0])
                    print(
                        '----------------------------------------------------------------->>>')

                elif 'tab_item_cap_img' in line:
                    # img_url
                    print(re.findall(
                        r'tab_item_cap_img"\ssrc="(.+?)"\s>', line)[0])
                    discount_img.append(re.findall(
                        r'tab_item_cap_img"\ssrc="(.+?)"\s>', line)[0])
                elif 'discount_block tab_item_discount' in line:
                    print(R + 'discount_original_price = ' + re.findall(
                        r'<div\sclass="discount_original_price">(.+?)</div>', line)[0] + W)
                    print(G + 'discount_pct = ' +
                          re.findall(r'<div\sclass="discount_pct">(.+?)</div>', line)[0] + W)
                    print(B + 'discount_final_price = ' +
                          re.findall(r'<div\sclass="discount_final_price">(.+?)</div>', line)[0] + W)

                    discount_original_price.append(re.findall(
                        r'<div\sclass="discount_original_price">(.+?)</div>', line)[0])
                    discount_pct.append(re.findall(
                        r'<div\sclass="discount_pct">(.+?)</div>', line)[0])
                    discount_final_price.append(re.findall(
                        r'<div\sclass="discount_final_price">(.+?)</div>', line)[0])

            except OSError:
                pass
    print('Done')


if __name__ == '__main__':
    File_Checker()
    Steam_Spider()
    Output()
