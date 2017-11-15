cd code
for D in `find . -type d`
do
    (cd $D && python test.py)
done
