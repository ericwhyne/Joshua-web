#!/bin/bash
read a
#echo $a
echo $a | sh /opt/joshua-v6.0.1/prepare.sh | nc localhost 5674
