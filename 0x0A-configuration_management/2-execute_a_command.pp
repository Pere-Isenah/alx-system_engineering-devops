# Define a new exec resource to kill the process named "killmenow"
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
