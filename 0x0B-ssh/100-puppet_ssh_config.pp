# config ssh
include stdlib

file_line {'identity file':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    replace => true,
}
file_line {'password no':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    replace => true,
}
