<h1>Video Feature</h1>

This part mainly records video feature
<img width="4191" alt="video dessert" src="https://user-images.githubusercontent.com/37787934/155257003-e5ca18c6-b231-4424-b3e4-6ab458b60f22.png">

<h2>What's M3U8?</h2>
e.g<br>
"m3u8": "#EXTM3U\n#EXT-X-TARGETDURATION:10\n#EXTINF:9,\nhttp://xxx.ts?start=0&end=xxxx&contentlength=xxxx&........=0\n#EXTINF:9,\nhttp:xxxx0.ts?start=xxxx&end=xxx&contentlength=xxxx&......=0\n
...#EXTINF:9,\nhttp:xxx.ts?start=xxxx&end=xxx&contentlength=xxx&.....=0\n#EXTINF:9....<br>
In this m3u8, it owns different xxx.ts file with end and start tag.<br>
When user watching video, it can be displayed from one ts to another ts file without load whole video file, 
which is all m3u8 file.<br>
`**So, what's the advantage user this way?**<br>
1. It makes the video more smooth with less stuck.<br>
2. If there's ABS, it helps seerver to make more effective bitrate.<br>
3. Under worse network, it can be much useful to support the video can always display without stop(stuck too long).<br>
`