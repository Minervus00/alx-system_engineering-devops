#!/usr/bin/env ruby
# Matches a phone number of ten digits 
puts ARGV[0].scan(/^\d{10}$/)
