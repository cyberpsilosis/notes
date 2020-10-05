# **Lab 07:** Analyze and Differentiate Types of Attacks and Mitigations Techniques

## **Bruteforcing SSH**

**Demostrate Ncrack Against denyhosts**
- Open Terminal
- Verify that the SSH service is running
```
~$ ps -eaf | grep HOSTS_DENY etc/denyhosts.conf | grep -v grep | grep sshd
```
- Verify that the service **denyhosts** is not running
```
~$ service denyhosts status
```
