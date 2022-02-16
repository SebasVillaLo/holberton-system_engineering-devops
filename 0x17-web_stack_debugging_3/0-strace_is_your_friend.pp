# Fiz error 500 Internal server error
exec{'fix-500':
  command => 'sed -i \'s/class-wp-locate.php/class-wp-locate.php/g\' /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
