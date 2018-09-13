# Puppet script to autromate  debug using strace
exec {'corrrect filetype':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  path    => ['/bin'],
}
