#!/bin/bash

echo "[1] binary to decimal"
echo "[2] decimal to binary"
echo "[3] hex to decimal"
echo "[4] decimal to hex"
echo "[5] binary to hex"
echo "[6] hex to binary"

echo ""

echo "select conversion method"
read CHOICE
echo "select value to convert"
read val

#choice 1

[ $CHOICE = "1" ] && echo "$((2#$val))"

#choice 2

[ $CHOICE = "2" ] && echo "obase=2;$val" | bc

#choice 3

[ $CHOICE = "3" ] && echo "$((16#$val))" | bc

#choice 4

[ $CHOICE = "4" ] && echo "obase=16;$val" | bc

#choice 5

[ $CHOICE = "5" ] && echo "obase=16;ibase=2;$val" | bc

#choice 6

[ $CHOICE = "6" ] && echo "obase=2;ibase=16;$val" | bc
