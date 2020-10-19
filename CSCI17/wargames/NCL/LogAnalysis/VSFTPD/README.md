**Sort Occurrences**
```
cat vsftpd.log | awk '{print $12}' | sort -n | uniq -c | sort -rn | head -n 15
```
**Match**
```
awk '/DOWNLOAD/{ print $14 }' vsftpdBBallPicsDownloads.txt > vsftpdBBallBytes.txt
```
**Add**
```
cat totalsDownloads.txt | paste -sd+ - | bc
```
