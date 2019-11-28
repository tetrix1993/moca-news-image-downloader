import argparse
import math
from myutil.util import create_directory
from myutil.util import download_image
from myutil.util import get_response
from myutil.util import is_dir_exists
from myutil.util import is_file_exists
from myutil.util import post_response

parser = argparse.ArgumentParser()
parser.add_argument('ID', help = 'Example: 20191016/2019101622300a_')
args = parser.parse_args()

PAGE_PREFIX = "https://moca-news.net/article/"
COOKIE_URL = "https://moca-news.net/pd.php"

BASE_FOLDER = "moca-news"
        
def check_str(art_id, img_id):
    check_chr = "abcdefghijklmnopqrstuvwxyz0123456789"
    root_chr = "020305071113"
    wk_check_str = "-"
        
    for i in range(0, 11, 2):
        temp = math.floor(( \
            pow(int(art_id[0:4]),(1 / int(root_chr[i:i+2])) \
            ) + pow(int(art_id[4:8]),(1 / int(root_chr[i:i+2])) \
            ) + pow(int(art_id[8:12]),(1 / int(root_chr[i:i+2])) \
            ) + pow(int(img_id),(1 / int(root_chr[i:i+2])))) * 100000) % 36
        wk_check_str += check_chr[temp:temp+1]
    return wk_check_str
    
def run(article_id):
    
    page_url = PAGE_PREFIX + article_id + "/01/"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    try:
        response = get_response(page_url, headers)
        article_id_split = article_id.split("/")
        if len(article_id_split) < 2:
            return
        art_id = article_id_split[1]
        data = {}
        data['art_id'] = art_id
        save_folder = BASE_FOLDER + "/" + art_id
        if not is_dir_exists(save_folder):
            create_directory(save_folder)
        split1 = response.split('<img src="../image/!')
        num_of_images = len(split1) - 1
        for i in range(num_of_images):
            pic_num = str(i + 1).zfill(2)
            if is_file_exists(save_folder + "/" + pic_num + ".jpg"):
                continue
            cookie = post_response(COOKIE_URL, headers, data)
            img_id = str(i + 1).zfill(3)
            image_page_url = PAGE_PREFIX + article_id + "/image" + img_id + ".html"
            image_url = PAGE_PREFIX + article_id + "/image/" + img_id + check_str(art_id, img_id) + ".jpg"
            headers['Cookie'] = 'imgkey' + img_id + '=' + str(cookie)
            filepathWithoutExtension = save_folder + "/" + pic_num
            download_image(image_url, filepathWithoutExtension, headers)
    except Exception as e:
        print(e)
            
if __name__ == '__main__':
    run(args.ID)
