# **Lab 07:** Analyze and Differentiate Types of Attacks and Mitigations Techniques

## **Bruteforcing SSH**

### **Demostrate Ncrack Against denyhosts**
**From Target Machine**
- Open Terminal
- Verify that the SSH service is running
```
~$ ps -eaf | grep -v grep | grep sshd
```
- Verify that the service **denyhosts** is not running
```
~$ service denyhosts status
```
- Based on the denyhosts.conf file, check to see where it places denied hosts.
```
~$ sudo grep HOSTS_DENY /etc/denyhosts.conf | grep -v "#"
```
**From Attacking Machine**
- Open Terminal
- Test SSH connection to the target system
```
~$ ssh name@ipaddress "uptime"
```
**From Target Machine**
- Open Terminal
- Grep the log entry recorded from the SSH connection that was initiated by the attacker.
```
~$ grep “Accepted password” /var/log/auth.log | grep “Attacker's IP”
```
**From Attacking Machine**
- Open Terminal
- Initiate the Ncrack tool against Ubuntu’s SSH service, using a predefined password list.
```