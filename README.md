![](music-tag.png)
# Music Tag Web
『音乐标签』Web版是一款可以编辑歌曲的标题，专辑，艺术家，歌词，封面等信息的应用程序， 支持FLAC, APE, WAV, AIFF, WV, TTA, MP3, MP4, M4A, OGG, MPC, OPUS, WMA, DSF, DFF等音频格式，绿色无广告，无任何功能限制。
# Why me
为什么开发web版？
在使用Navidrome时，我的音乐都是在远程服务器上的，本地的Musictag和mp3tag不能满足我的需求，
我需要部署在远程服务器上去需改线上的音乐标签，相当于在使用Navidrome的边车应用。
- 该版本是我自用的小工具，如果你也有这个需求，可以使用。欢迎提出issues，我会满足你的需求，在我的能力范围内。
# How to Build
1. docker-compose -f local.yml build
2. docker-compose -f local.yml up
# How to Use
镜像已上传至阿里云Docker Registry
操作指南：
1. `docker login --username=xxx registry.cn-hangzhou.aliyuncs.com`
2. `docker pull registry.cn-hangzhou.aliyuncs.com/charles0519/music_tag_web:0.05`
3. docker-compose.yml / portainer stacks
![img_1.png](img_1.png)
```yaml
version: '3'

services:
  music-tag:
    image: registry.cn-hangzhou.aliyuncs.com/charles0519/music_tag_web:0.5
    container_name: music-tag-web
    ports:
      - "8001:8001"
    volumes:
      - D:\Music:/app/media:z
    command: /start
    restart: always
```
# User Interface 
![](img.png)
![img_3.png](img_3.png)
![img_2.png](img_2.png)