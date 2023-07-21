# This Puppet manifest increases the amount of traffic an Nginx server can handle.

# Step 1: Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Step 2: Restart Nginx after the configuration change
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix--for-nginx'],
}

# This Puppet manifest allows the user 'holberton' to login and open files without errors.

# Step 3: Increase the hard file limit for the Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Step 4: Increase the soft file limit for the Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
