# Create a new file
file { '/tpm/school':
    mode     => '0744',
    owner    => 'www-data',
    group    => 'www-data',
    contains => 'I love Puppet',
}
