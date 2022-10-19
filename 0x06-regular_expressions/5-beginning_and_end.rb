#!/usr/bin/env ruby
# Matches a word with pattern h + a_single_caracter + n 
puts ARGV[0].scan(/h\w{1}n/)
