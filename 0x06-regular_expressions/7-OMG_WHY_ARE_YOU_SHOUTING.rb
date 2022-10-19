#!/usr/bin/env ruby
# Matches capital letters in a string and prints them in the same line
puts ARGV[0].scan(/[A-Z]/).join
