breakpoint set source.cpp -l 9
breakpoint set source.cpp -l 13
breakpoint set source.cpp -l 16 -o
breakpoint set source.cpp -l 28
breakpoint set source.cpp -l 34 -o
breakpoint set source.cpp -l 36
9========================= run
expression int $backup[3]
//watchpoint set variable tab[1]
//watchpoint command add 1
13 ======================== continue
n
thread step-out
expr $backup[count] = tab[1]
continue
n
expr $backup[count] = tab[1]
continue
n
expr $backup[count] = tab[1]
16 ========================== continue
expression expr for (int i = 0; i < 3; i++) tab[i] = $backup[i];
expression count = 0
28========================= continue
expression tmp = ($backup[0] + $backup[1] + $backup[2]) / max
34========================= continue
expression i = 0
36========================= continue
expression biggest = min[i]
==========================continue
