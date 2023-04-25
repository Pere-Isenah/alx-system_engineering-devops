#!/usr/bin/puppet
# configures ssh with puppet

include stdlib

file_line { 'nopwd':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}
file_line { 'identity':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/id_rsa',
  path   => '/etc/ssh/ssh_config',
}