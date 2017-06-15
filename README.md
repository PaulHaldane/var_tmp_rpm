# var_tmp_rpm
demo RPM that changes permissions on a system folder 

Created as part of investigation of issues with permissions on /var/tmp being repeatedly broken. We eventually realised that 
this happened after installation of a set of packages (which we do regularly as part of testing).

CentOS 5.x will silently change the permissions. An rpm built from the same spec file on CentOS 7.x won't install without --force.
