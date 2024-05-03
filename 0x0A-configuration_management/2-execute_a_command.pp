# kills a running process
exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  environment => ['PATH=/bin:/usr/bin:/usr/sbin'],
}
