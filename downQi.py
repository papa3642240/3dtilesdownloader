import requests
import os
import getopt

def getFileNameFromUrl(url):
    str_list = url.split('/')
    return str_list[-1]


def downLoad(url,savedir):

    if not os.path.exists(savedir):
        os.makedirs(savedir)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'data.mars3d.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    r = requests.get(url,  headers=headers)
    # 保存
    fileName = getFileNameFromUrl(url)
    with open(savedir+"/"+fileName, 'wb') as f:
        f.write(r.content)
        f.close


if __name__ == '__main__':

    baseurl = ''
    savedir = ''
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:d:", ["url=", "dir="])
    except getopt.GetoptError:
        print('param error')
        pause()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--url"):
            baseurl = arg
        elif opt in ("-d", "--dir"):
            savedir = arg

    if baseurl == '':
        print('please input url param or use --help to see how to use it')
        pause()
        sys.exit(2)
    if savedir == '':
        print('please input dir param or use --help to see how to use it')
        pause()
        sys.exit(2)
        
    downLoad(baseurl,savedir)
    os.system('pause')
