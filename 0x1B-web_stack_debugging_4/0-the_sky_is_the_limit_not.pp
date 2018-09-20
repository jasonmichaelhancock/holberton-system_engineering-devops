# Change file limit parameter

exec { 'increase_fileno_limit':
  command => 'sed -i "${} a ULIMIT=\"-n 2048\"" /etc/default/nginx',
  path    => [ '/bin/' ]
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => [ '/usr/bin/' ]
}
