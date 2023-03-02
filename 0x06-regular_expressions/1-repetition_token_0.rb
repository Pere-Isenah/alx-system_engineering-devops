#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching 
#"hbttn","hbtttn","hbttttn","hbtttttn"

puts ARGV[0].scan(/hbt{2,5}n/)