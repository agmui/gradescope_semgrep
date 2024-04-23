#!/bin/bash

# shellcheck disable=SC2164
cd $SRC_DIR # Defined in Gradescope_setup/autograder/run_autograder

# TODO: make it a global func like clone_dir
find_and_mv () {
  DESTINATION="$1"   # Save first argument in a variable
  shift            # Shift all arguments to the left (original $1 gets lost)
  FILES=("$@") # Rebuild the array with rest of arguments
  echo ==== searching for FILES =====
  for f in "${FILES[@]}"
  do
    echo --  searching for: $f  --

    # if already at target destination
    if [ -f "$DESTINATION/$f" ]; then
      echo found file: "$DESTINATION/$f"
      continue
    fi
    file_path=$(find "$DESTINATION" -maxdepth 20 -name "$f" -print -quit)
    if  [ -z "$filepath" ]; then
      echo found path: "$file_path"
      mv $file_path $DESTINATION
    else
      echo cound not find file
    fi
  done
  echo ==============================
}

find_and_mv /autograder/submission factoring.c threadSort.c add_a_lot.c red_blue_purple.c

cp -r /autograder/submission/* $SRC_DIR


#make > /dev/null
#gcc -Wall -g -pthread -c -pthread -ggdb factoring.c -o thread_factoring.bin
#gcc -Wall -g -pthread -c -pthread -ggdb threadSort.c -o thread_sort.bin
#gcc -Wall -g -pthread -c -pthread -ggdb add_a_lot.c -o basic_mutex.bin
#gcc -Wall -g -pthread -c -pthread -ggdb red_blue_purple.c -o red_blue_purple.bin
gcc -pthread -ggdb factoring.c -o factoring.bin
gcc -pthread -ggdb threadSort.c -o thread_sort.bin
gcc -pthread -ggdb add_a_lot.c -o basic_mutex.bin
gcc -pthread -ggdb red_blue_purple.c -o red_blue_purple.bin

cd $SRC_DIR/..
echo "--- running run_tests.py ---"
python3 run_tests.py
