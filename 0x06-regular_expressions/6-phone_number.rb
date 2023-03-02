#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching 
#a 10 digit phone number

puts ARGV[0].scan(/^\d{10}/)