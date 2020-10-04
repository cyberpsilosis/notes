
# **SSH Login Credentials (Flags)**

## **Host**
**Domain:** bandit.labs.overthewire.org
**Port:** 2220

## **Level 0**
Username: bandit0<br>
Password: bandit0

**Commands Used:** ssh, ls, cat

## **Level 1**
Username: bandit1<br>
Password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

**Commands Used:** ssh, ls, cd, cat

## **Level 2**
Username: bandit2<br>
Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

**Commands Used:** ssh, ls, cd, cat

## **Level 3**
Username: bandit3<br>
Password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

**Commands Used:** ssh, ls, cd, cat

## **Level 4**
Username: bandit4<br>
Password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

**Commands Used:** ssh, ls, cd, cat

## **Level 5** 
Username: bandit5<br>
Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

**Commands Used:** ssh, ls, cd, cat

## **Level 6** 
Username: bandit6<br>
Password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

**Flag Properties:**
- human-readable
- 1033 bytes in size
- not executable

**Commands Used:** ls, cd, find

    ~$ find / -size +50M -iname "filename"

- Filter by size. 
- This will return results that are 50 megabytes or larger.
- You can use + or - to search for greater or lesser sizes. 
- Omitting = will search for files exactly the specified size.
- You can filter by bytes (c), kilobytes (k), megabytes (M), gigabytes (G), or 512-byte blocks (b). Note that the size flag is case-sensitive.

## **Level 7**
Username: bandit7<br>
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

**Flag Properties:**
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

**Commands Used:** man find grep cat

    ~$ find / -user bandit7 -group bandit6 -size 33c 2>&1 | grep -F -v Permission

- Use man to learn the command options

## **Level 8**
Username: bandit8<br>
Password: 

## **Level 9**
Username: bandit9<br>
Password: 

## **Level 10*
Username: bandit10<br>
Password: 

## **Level 11**
Username: bandit11<br>
Password: 

## **Level 12**
Username: bandit12<br>
Password: 

## **Level 13**
Username: bandit13<br>
Password: 
