#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching 
#"hbtn","hbttn","hbtttn","hbttttn"

puts ARGV[0].scan(/hbt{1,4}n/)