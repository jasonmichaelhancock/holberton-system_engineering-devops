# Change file limit parameter

exec { 'increase_fileno_limit':
  command => 'sed -i "s/15/10000/g" /etc/default/nginx',
  path    => '/bin/',
  onlyif  => 'test -e /etc/default/nginx',
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/bin/',
}
