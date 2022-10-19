#!/usr/bin/env ruby
# Matches hb + (0 or more) occurrences of t + n words
puts ARGV[0].scan(/hbt*n/)
