// https://en.wikipedia.org/wiki/Euclidean_algorithm

#include <stdio.h>
#include <stdlib.h>

int gcd(int i, int j) {
  if (j == 0) {
    return i;
  } else {
    return gcd(j, i % j);
  }
}

int main(int argc, char const *argv[]) {
  if (argc < 3) {
    printf("usage: %s <integer> <integer>\n", argv[0]);
    return 0;
  }

  int i = atol(argv[1]);
  int j = atol(argv[2]);

  int divisor = gcd(i, j);

  printf("%d\n", divisor);

  return 0;
}
