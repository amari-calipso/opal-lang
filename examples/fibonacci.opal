package opal: import *;

new function getInt() {
    while True {
        IO.out("Insert number of terms: ");
        new dynamic n = IO.read();

        try {
            n = int(n);
        } catch ValueError {
            IO.out("Invalid input. Retry.\n");
        } success {
            if n <= 0 {
                IO.out("Invalid input. Retry.\n");
                continue;
            }

            return int(n);
        }
    }
}

main() {
    new int n = getInt();

    new int a = 0,
            b = 1, c;

    for i = 0; i < n; i++ {
        IO.out(a, IO.endl);
        c = a + b;
        a = b;
        b = c;
    }
}