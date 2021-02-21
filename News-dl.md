
**WEB UI  Docker**

https://github.com/manbearwiz/youtube-dl-server  

```

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl      
sudo chmod a+rx /usr/local/bin/youtube-dl        

docker run -d --net="host" --name youtube-dl -v /root/Docker:/youtube-dl kmb32123/youtube-dl-server         

说明：  -v   本地目录:Docker内目录        


打开  WEB页面：  http://10.252.x.x:8080/youtube-dl           


```



**下载视频和字幕**

```
youtube-dl  --all-subs       -f http-5192   /cbs-evening-news/
```

*字幕转换*
```
ffmpeg -i source.en.vtt target.en.srt

```




**查看视频格式**
```
youtube-dl -F    /bs-weekend-news/
```
**查看字幕**
```
youtube-dl --list-subs   /cbs-weekend-news/
```
**字幕相关的命令**
```
--write-sub                      Write subtitle file
--write-auto-sub                 Write automatic subtitle file (YouTube only)
--all-subs                       Download all the available subtitles of the video
--list-subs                      List all available subtitles for the video
--sub-format FORMAT              Subtitle format, accepts formats preference, for example: "srt" or "ass/srt/best"
--sub-lang LANGS                 Languages of the subtitles to download (optional) separated by commas, use IETF language tags like 'en,pt'
```
