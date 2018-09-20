# Change file limit parameter

exec { 'increase_fileno_limit':
  path     => ['/bin'],
  command  => 'sed -i \"s/15/50000/g\" /etc/default/nginx',
}
exec { 'restart nginx':
  path     => ['/usr/bin'],
  command  => 'sudo service nginx restart',
}
