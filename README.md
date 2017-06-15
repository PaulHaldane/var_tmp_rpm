# var_tmp_rpm
demo RPM that changes permissions on a system folder 

Created as part of investigation of issues with permissions on /var/tmp being repeatedly broken. We eventually realised that 
this happened after installation of a set of packages (which we do regularly as part of testing).

CentOS 5.x will silently change the permissions. An rpm built from the same spec file on CentOS 7.x won't install without --force.


## CentOS 7.3

```
[vagrant@localhost paul1]$ sudo rpm -i ~/rpmbuild/RPMS/x86_64/var_tmp-1.0-1.x86_64.rpm
        file /var/tmp from install of var_tmp-1.0-1.x86_64 conflicts with file from package filesystem-3.2-21.el7.x86_64
[vagrant@localhost paul1]$ rpm -q var_tmp
package var_tmp is not installed
[vagrant@localhost paul1]$ ls -ld /var/tmp
drwxrwxrwt. 7 root root 4096 Jun 15 14:39 /var/tmp

[vagrant@localhost paul1]$ sudo rpm -i ~/rpmbuild/RPMS/x86_64/var_tmp-1.0-1.x86_64.rpm --force
[vagrant@localhost paul1]$ ls -ld /var/tmp
drwxrwx---. 7 root root 4096 Jun 15 14:39 /var/tmp
```

## CentOS 5.11

```
[vagrant@localhost ~]$ sudo rpm -i ~/rpmbuild/RPMS/x86_64/var_tmp-1.0-1.x86_64.rpm
[vagrant@localhost ~]$ ls -dl /var/tmp
drwxrwx--- 5 root root 4096 Jun 15 14:29 /var/tmp
```
