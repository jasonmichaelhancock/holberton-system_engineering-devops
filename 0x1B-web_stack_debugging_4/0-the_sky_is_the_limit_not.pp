# Change file limit parameter

$settings = '/etc/default/nginx'
file { $settings:
  ensure => present,
}
exec { 'increase_fileno_limit':
  command => "sed -i 's/15/15000/' ${settings}",
  path    => [ '/bin/' ]
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => [ '/usr/bin/' ]
}
