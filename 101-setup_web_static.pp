# sets up your web servers for the deployment of web_static

exec { 'update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/usr/sbin'],
}

exec { 'upgrade':
  command => '/usr/bin/apt-get -y upgrade',
  path    => ['/usr/bin', '/usr/sbin'],
  require => Exec['update'],
}

package { 'nginx':
  ensure   => 'installed',
  require => Exec['upgrade'],
}

file { '/data':
  ensure   => directory,
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static':
  ensure   => directory,
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure   => 'directory'  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure   => 'directory',
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure   => 'directory',
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure   => 'present',
  content  => '',
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

file { '/data/web_static/current':
  ensure   => 'link',
  target   => '/data/web_static/releases/test',
  owner    => 'ubuntu',
  group    => 'ubuntu',
}

exec { 'nginx_config':
  command => "/bin/sed -i '38i\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current;\\n\\t}\\n' /etc/nginx/sites-available/default",
  path    => ['/bin', '/usr/sbin'],
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['nginx_config'],
}
