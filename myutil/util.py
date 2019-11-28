import requests
import urllib.request
import os

#Need install requests: run "pip install requests"

def get_response(url, headers=None, decode=False):
    response = ""
    if headers == None:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    try:
        result = requests.get(url, headers=headers)
        if (decode):
            response = str(result.content.decode())
        else:
            response = str(result.content)
    except Exception as e:
        print(e)
    return response

def post_response(url, headers=None, data=None):
    response = ""
    if headers == None:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    try:
        result = requests.post(url, headers=headers, data=data)
        response = str(result.content.decode())
    except Exception as e:
        print(e)
    return response

def is_file_exists(filepath):
    return os.path.isfile(filepath)
    
def is_dir_exists(filepath):
    return os.path.isdir(filepath)

def download_image(url, filepathWithoutExtension, headers=None):
    if ".png" in url:
        filepath = filepathWithoutExtension + ".png"
    elif ".jpeg" in url:
        filepath = filepathWithoutExtension + ".jpeg"
    elif ".gif" in url:
        filepath = filepathWithoutExtension + ".gif"
    else:
        filepath = filepathWithoutExtension + ".jpg"
        
    # Check local directory if the file exists
    if (is_file_exists(filepath)):
        #print("File exists: " + filepath)
        return False
        
    if headers == None:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        
    # Download image:
    try:
        with requests.get(url, stream=True, headers=headers) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print("Downloaded " + url)
        return True
    except Exception as e:
        print("Failed to download " + url)
        print(e)
        return False

def create_directory(filepath):
    # If directory exists
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def to_valid_name(name):
    return name.replace(' ','_').replace(':','').replace('\\','_').replace('/','_').replace('*','') \
        .replace('"',"'").replace('?','').replace('<','').replace('>','').replace('|','')
