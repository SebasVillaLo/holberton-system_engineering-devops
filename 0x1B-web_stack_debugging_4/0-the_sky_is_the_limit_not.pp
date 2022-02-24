# Request limit
exec {'sed -i "s/15/4096/" /etc/default/nginx':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell
}

exec {'sudo service nginx restart':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell
}
