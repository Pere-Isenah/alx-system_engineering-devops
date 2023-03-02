#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching 
#"hbn","hbtn","hbttn","hbtttn","hbttttn"

puts ARGV[0].scan(/hbt*n/)