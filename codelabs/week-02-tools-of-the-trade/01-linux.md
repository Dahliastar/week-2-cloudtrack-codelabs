# Part 1: Linux essentials

Why it matters: almost every cloud server and container runs Linux. You will live in a terminal.

## Checkpoint 0: where am I?
```bash
pwd          # print working directory
ls -la       # list all files with details
whoami
```

## Checkpoint 1: navigate and build
```bash
mkdir -p playground/notes/week2
cd playground
touch hello.txt
echo "cloud track" > hello.txt
echo "week 2" >> hello.txt
cat hello.txt
```
`>` overwrites, `>>` appends. Try swapping them and see what happens.

## Checkpoint 2: copy, move, delete
```bash
cp hello.txt notes/copy.txt
mv notes/copy.txt notes/week2/renamed.txt
rm hello.txt
rm -r notes        # -r for directories. There is no recycle bin.
```

## Checkpoint 3: search and pipe
```bash
printf "alpha\nbeta\nalphabet\n" > words.txt
grep alpha words.txt
grep -c alpha words.txt
cat words.txt | sort | uniq
ls -la | grep words
```

## Checkpoint 4: permissions
```bash
echo 'echo "I ran!"' > run.sh
ls -l run.sh         # note -rw-r--r--
./run.sh             # permission denied
chmod +x run.sh
./run.sh
```
Read `-rwxr-xr-x` as: owner / group / others, each with read, write, execute. Cloud IAM follows the same least-privilege idea.

## Think about it
1. What is the difference between `cd ..` and `cd -`?
2. Why is `rm -rf /` dangerous, and what makes `rm -rf $UNSET_VAR/` dangerous too?
