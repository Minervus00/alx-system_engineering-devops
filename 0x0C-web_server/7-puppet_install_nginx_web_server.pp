# Use Puppet Manifest to install and configure Nginx

exec { 'update':
  command => 'sudo sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'install':
  require => Exec['update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'main_page':
  require => Exec['install'],
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'conf':
  require     => Exec['main_page'],
  environment => ['GG=google.com permanent'],
  command     => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me $GG;/" /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}

exec { 'restart':
  require => Exec['conf'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
