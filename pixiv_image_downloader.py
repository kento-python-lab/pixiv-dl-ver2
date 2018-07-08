from pixivpy3 import *
from time import sleep
import os
import setting


# ピクシブ API へログイン
api = PixivAPI()
api.login(setting.pixiv_id, setting.client_password)
app_api = AppPixivAPI()

# 絵師のページIDを入力する
start_id_search = int(input('取得したい絵師のページID(start)を入力してください。>>>'))
end_id_search = int(input('取得したい絵師のページID(end)を入力してください。>>>')) + 1

# タグの指定
target_tag = str(input('取得タグを指定してください。>>>'))

# 保存先ディレクトリ名
image_dir = target_tag if target_tag != '' else 'other'

# 最大画像取得数
works = 300

separator = '------------------------------------------------------------'

# 保存先パスの生成
saving_directory_path = './Downloads/' + image_dir + '/'
if not os.path.exists(saving_directory_path):
    os.mkdir(saving_directory_path)

for id_search in range(start_id_search, end_id_search):
    sleep(2)
    print(separator)
    print(separator)
    print(f'target_id：  {id_search}')
    print(separator)
    try:
        illustrator_id = api.users_works(id_search, per_page=works)
        total_works = illustrator_id.pagination.total

        # 最大取得数が絵師の公開する画像の枚数以上の場合
        # 最大画像取得数を合計枚数にセット
        if works < total_works:
            total_works = works

        illust = illustrator_id.response[0]

        print('Illustrator: {}'.format(illust.user.name))
        print('Works number: {}'.format(total_works))
        print(separator)

        # ダウンロードスタート
        for work_no in range(0, total_works):
            try:
                illust = illustrator_id.response[work_no]

                if target_tag not in illust.tags and target_tag != '':
                    continue

                print('Now: {0}/{1}'.format(work_no + 1, total_works))
                print('Title: {}'.format(illust.title))

                if os.path.exists(saving_directory_path+str(illust.id)+'_p0.png')\
                        or os.path.exists(saving_directory_path + str(illust.id) + '_p0.jpg'):
                    # すでにダウンロード済みの場合スキップ
                    print('Title:'+str(illust.title)+' has already downloaded.')
                    print(separator)
                    sleep(1)
                    continue

                if illust.is_manga:
                    work_info = api.works(illust.id)
                    for page_no in range(0, work_info.response[0].page_count):
                        page_info = work_info.response[0].metadata.pages[page_no]
                        app_api.download(page_info.image_urls.large, saving_directory_path)
                        sleep(3)

                else:
                    app_api.download(illust.image_urls.large, saving_directory_path)
                    sleep(3)

            except:
                sleep(1)
                continue

            print(separator)

        print('Download complete!　Thanks to {}!!'.format(illust.user.name))

    except:
        sleep(1)
        continue

print(separator)
print(separator)
print('complete')
