# Using Puppet, create a manifest that kills a process named 'killmenow'

exec { 'kill a process':
  command   => 'pkill -f killmenow',
  provider  => 'shell'
}

