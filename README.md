![Logo](./doc/logo.png)

> 使用说明

```text
版本：V20201120.001
    使用说明：
         options:
             --url     / -u    需要下载的3dtiles数据，必填
             --dir     / -d    输出目录，必填")
             --start   / -s    开始下载的位置下标，默认从0开始，一般是分段下载或者某一个下载失败的时候使用
             --end     / -e    结束下载的位置下标，默认数据总长度，一般是分段下载或者某一个下载失败的时候使用
             --threads / -t    启动多线程下载，指定线程数，默认为1
             --help            查看帮助 
```

> 使用示例

`downloader.exe --url=https://lab.earthsdk.com/model/702aa950d03c11e99f7ddd77cbe22fea/tileset.json -d D:\3_Resources\3_数据\ddd -t 3`

> 注意事项

1. 基于Python 3.7.0开发
2. 路径中不要带中文
3. pyinstaller -F downloader.py 重新编译
4. 安装pyinstaller 执行命令 pip install pyinstaller -i https://pypi.mirrors.ustc.edu.cn/simple/ 临时使用国内的镜像地址 ---- 常用的国内镜像地址参考文章：https://blog.csdn.net/dss875914213/article/details/86500146

> 下载GLB模型步骤

1.  pyinstaller -F downQi.py 重新编译
2.  pycharm 专门开发Python的ide
3.  downQi.exe --url=http://data.mars3d.cn/gltf/mars/floor/top.glb -d C:\Users\admin\Desktop\data