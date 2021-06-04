a={"Bibash":21,"Biplov":22};
print(a["Bibash"]);


square= {1:1,2:4,3:"error"};
square[3]=9;
print(square);
print(square.get(1));
print(square.get(5));
print(1 in square);
print(2 not in square);




fib={1:1,2:2,3:2,4:3};
print(fib.get(3,0));
print(fib.get(7,5));
