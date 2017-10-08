#!/bin/bash

# Getting the input .iso file name
echo "Choose the ISO File:"
ls *.iso -1 | cat -n 
echo -n "Insert number: "
read image_number
a=1

for i in $(ls *.iso -1)
do
    if [ $image_number -eq $a ]
    then
        image=$i
        break
    else
        a=$((a = a + 1))
    fi
done
 
# Checks if the file exists and ends in .iso
if ((! [ -f $image ]) || (! [[ $image == *.iso ]]))
then
    echo "[Error]: Wrong file!"
    exit 2
fi

echo "You chose: $image"

echo "Which is the device you want to burn the ISO file on?"

# Lists the file systems
df | grep /dev/sd
echo "Insert device(for example, /dev/sdb1):"
read partition

# Checks if the given device is correct or else exits the script
if (! [[ $partition =~ /dev/sd[a-z][1-9] ]] || ! [[ -e $partition ]])
then
    echo "[Error]: Wrong device!"
    exit 3
fi

device="$(echo $partition | sed s'/.$//')"

# Device confirmation
echo "Are you sure $device($partition) is the device you want to burn your ISO file on?[y/n]"
while true
do
    read answer
    if [[ $answer == "yes" || $answer == "y" ]]
    then
        # Unmounting the partition 
        umount $partition
        echo "Please wait ..."

        # Burning the iso
        dd bs=4M if=$image of=$device
        sync
        echo "Done!"
        break
    fi

    if [[ $answer == "no" || $answer == "n" ]]
    then
        break
    fi
done

exit 0
