# Change file limit parameter

exec { 'increase_fileno_limit':
  command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2048\"/g" /etc/default/nginx',
  path    => [ '/bin/' ]
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => [ '/usr/bin/' ]
}
