
**Extract all IP addresses from a file:**
```
grep -oP '([01]?\d\d?|2[0-4]\d|25[0-5]).([01]?\d\d?|2[0-4]\d|25[0-5]).([01]?\d\d?|2[0-4]\d|25[0-5]).([01]?\d\d?|2[0-4]\d|25[0-5])' file.txt
```