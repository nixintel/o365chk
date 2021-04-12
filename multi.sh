for f in $(cat $1);
do python3 o365chk.py -d $f;
done;
