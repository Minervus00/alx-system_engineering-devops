# Using Puppet, create a file in /tmp

file { '/tmp/School'
	ensure => 'file'
	mode => '0744'
	owner => 'www-data'
	group => 'www-data'
	content => 'I love Puppet'
}
