// https://en.wikipedia.org/wiki/Collatz_conjecture

#include <stdio.h>
#include <stdlib.h>

int collatz(long n) {
  int len = 0;

  while (n > 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = n * 3 + 1;
    }
    printf("%ld\n", n);
    len = len + 1;
  }

  if (n < 0) {
    printf("overflowed\n");
  }

  return len;
}

int main(int argc, char const *argv[]) {
  long n = 0;
  int len = 0;
  if (argc < 2) {
    printf("usage: %s <integer>\n", argv[0]);
    return 0;
  }

  n = atol(argv[1]);
  printf("integer: %ld\n", n);

  printf("sequence:\n");
  len = collatz(n);

  printf("length: %d\n", len);

  return 0;
}
