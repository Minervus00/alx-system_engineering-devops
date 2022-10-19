#!/usr/bin/env ruby
# Matches hb + (2, 3, 4 or 5) occurrences of t + n words
puts ARGV[0].scan(/hbt{2,5}n/).join
