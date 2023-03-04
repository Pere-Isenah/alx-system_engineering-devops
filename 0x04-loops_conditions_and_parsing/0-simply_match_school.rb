#!/usr/bin/env ruby
regex = /School/
input = ARGV[0]

p input =~ regex ? #{input} : No match found.
