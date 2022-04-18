from selenium import webdriver



max_cnt = 20 # 최대 받는 갯수 설정
keyword = "wallpaper" #여러가지 다른 소스를 받을수도 있기 때문에 키워드를지정한다.
urls = f'https://www.pexels.com/ko-kr/search/{keyword}/'
chromedriver = 'C:\Users\ChO\Desktop\Workplace\practice\auto_download_img\chromedriver.exe'


browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get(urls) #위 설정한 url로 접속

# photo_items = browser.find_elements_by_class_name(('photo-item__img')) 
# #구글에서 이미지 - 검사 를 통해 클래스를 확인한 후 클래스명을 넣어줘야함
# img_urls = [x.get_attribute('data-big-src') for x in photo_items]
# #홈페이지에서 확인한 데이터 빅 소스에서 이미지가 바로 뜨기 때문에 데이터 빅스소를 바로 넣어줌

# idx=1
# for img_url in img_urls:
#     browser.get(img_urls)
#     res = requests.get(img_urls)
#     if res.ok:
#         file_name = f'{keyword}_{idx}.jpeg'
#         with open(file_name,'wb') as f:
#             f.write(res.content)
#         print(f'({idx}){file_name}')#(2) wallpaper_2 .jpg
#         idx +=1

#     if idx > max_cnt:
#         break

# browser.quit()