

**$cat netflowNOport.txt | awk '{print $6}' | sort -n | uniq -c | sort -rn | head -n 15**
```
   1784 102.85.184.239
    820 233.186.34.242
    212 193.33.231.196
    109 193.104.41.89
     59 59.45.79.40
     50 59.47.0.148
     45 116.195.145.12
     26 104.238.221.67
     22 59.45.79.117
     18 119.146.221.68
     17 46.148.18.162
     16 185.130.5.200
     15 85.25.1.208
     15 58.218.211.198
     15 218.57.11.7
```