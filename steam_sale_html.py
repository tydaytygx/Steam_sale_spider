import requests
import urllib
import urllib.request
import re
import os
import shutil


def createFile(filePath):

    if os.path.exists(filePath):  # If folder exists
        shutil.rmtree('img')
    else:  # File doesn't exist
        print('No such file:%s' % filePath)

    if os.path.exists(filePath):
        print('%s: exists' % filePath)
    else:
        try:
            os.mkdir(filePath)
            print('New folder：%s' % filePath)
        except Exception as e:
            os.makedirs(filePath)
            print('New multi-sub-folder：%s' % filePath)

def File_Checker():  # Check if output files exist or not

    if(os.path.exists('steam_sale.html')):
        os.remove('steam_sale.html')  # Check html file
    elif(os.path.exists('steam_saleout.md')):
        os.remove('steam_saleout.md')  # Check output file


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

        f = open('steam_sale.html', 'a', encoding='UTF-8', errors='ignore')
        print(r.text, file=f)

        f.close()
        print('Completed with ' + r.encoding)  # Site 's HTML encoding
        page = page + 1

def getNonRepeatList(data):  # No-repeat tool
    return [i for n, i in enumerate(data) if i not in data[:n]]


def Output():
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
                    print('discount_original_price = ' + re.findall(
                        r'<div\sclass="discount_original_price">(.+?)</div>', line)[0])
                    print(
                        'discount_pct = ' + re.findall(r'<div\sclass="discount_pct">(.+?)</div>', line)[0])
                    print('discount_final_price = ' +
                          re.findall(r'<div\sclass="discount_final_price">(.+?)</div>', line)[0])

                    discount_original_price.append(re.findall(
                        r'<div\sclass="discount_original_price">(.+?)</div>', line)[0])
                    discount_pct.append(re.findall(
                        r'<div\sclass="discount_pct">(.+?)</div>', line)[0])
                    discount_final_price.append(re.findall(
                        r'<div\sclass="discount_final_price">(.+?)</div>', line)[0])

            except OSError:
                pass

    # Output as a file
    with open('steam_saleout.html', 'w', encoding='UTF-8', errors='ignore') as f3:
        print(r'''
        <!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			
			*{
				transition-duration: 0.5s;
				margin: 0;
				word-break: break-all;
				box-sizing: border-box;
				transition-duration: 0.5s;
				font-family: "microsoft yahei";
				color: white;
			}
			body{
				background-color: #24292e;
			}
			div:hover{
				border: none;
				font-size: 20px;
				background-color: #5b5b5b;
				width: 100%;
				
			}
			
			.discount_original_price{
				background-color: cornflowerblue;
				width: 100%;
				background-color: #2894ff;
				border-radius: 5px 5px 5px 5px;
			}
			
			.discount_pct{
				background-color: cornflowerblue;
				width: 100%;
				background-color: #73bf00;
				border-radius: 5px 5px 5px 5px;
			}
			
			.discount_final_price{
				
				background-color: cornflowerblue;
				width: 100%;
				background-color: #ff8040;
				border-radius: 5px 5px 5px 5px;
				
			}
			
			.hover_check{
				display: block;
				background-color: #24292e;
				width: 0%;
			}
			.hover_check:hover{
				background-color: indianred;
				width: 100%;
			}
		</style>
	</head>
	<body>''', file=f3)

        for v in range(len(discount_name)):

            if '/' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '/', ''))  # When using urlretrieve, the : makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('/', ''), file=f3)

            elif '/' in discount_name[v] and ':' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '/', ''))  # When using urlretrieve, the : makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('/', ''), file=f3)

            elif ':' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    ':', ''))  # When using urlretrieve, the : makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace(':', ''), file=f3)
            elif '|' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '|', ''))  # When using urlretrieve, the | makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('|', ''), file=f3)

            elif '?' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '?', ''))  # When using urlretrieve, the | makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('|', ''), file=f3)

            elif ',' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    ',', ''))  # When using urlretrieve, the | makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('|', ''), file=f3)

            elif '@' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '@', ''))  # When using urlretrieve, the | makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('@', ''), file=f3)

            elif '&amp' in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '&amp', ''))  # When using urlretrieve, the | makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('&amp', ''), file=f3)

            elif '*' in discount_name[v] in discount_name[v]:
                urllib.request.urlretrieve(discount_img[v], 'img\%s.jpg' % discount_name[v].replace(
                    '*', ''))  # When using urlretrieve, the : makes files can't be save completely
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v].replace('/', ''), file=f3)

            else:
                urllib.request.urlretrieve(
                    discount_img[v], 'img\%s.jpg' % discount_name[v])
                print(r'<div><p class="hover_check hover_check:hover"><img src="img\%s.jpg" class="multiimage 3d_show"/ > </div></p>' %
                      discount_name[v], file=f3)

            print('# ' + discount_name[v], file=f3)
            # Game's Discount_before, transformating would be a little bit slower than the others?
            print(r'<b class="discount_original_price" >discount_original_price = %s</b>' %
                  discount_original_price[v], file=f3)
            print(r'<b class="discount_pct" >discount_pct = %s</b>' %
                  discount_pct[v], file=f3)  # Game's Discount
            print(r'<b class="discount_final_price" > discount_final_price = %s</b>' %
                  discount_final_price[v], file=f3)  # Game's Discounted
            # print('-------------------', file = f3)
        print(r'''
    </body>
</html>''', file=f3)

    print('done')


if __name__ == '__main__':
    createFile(os.getcwd() + '\img')
    File_Checker()
    Steam_Spider()
    Output()
