# Change file limit parameter

exec { 'increase_fileno_limit':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sed -i "s/15/64000/g" /etc/default/nginx',
}
exec { 'restart nginx':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo service nginx restart',
}
