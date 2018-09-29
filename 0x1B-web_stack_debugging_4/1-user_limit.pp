# Change the OS configuration so that it is possible
# to login with the holberton user and open a file without any error message.
exec { 'increase file limits':
  command => 'sudo sed -i "s/4/4000/g" /etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'test -e /etc/security/limits.conf',
}
