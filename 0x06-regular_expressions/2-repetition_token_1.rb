#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching 
#"htn","hbtn"

puts ARGV[0].scan(/hb{0,1}tn/)