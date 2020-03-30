#include <stdlib.h>
#include <stdio.h>
#include <time.h>

const int TEST_COUNT = 1000000;
const int TRADE_COUNT = 1000000;
const int STOP_LIMIT = -10;

static inline int random_pnl()
{
    return rand() & 0x1 ? 1 : -1;
}

static inline int trade()
{
    int pnl = 0;

    for (size_t i = 0; i < TRADE_COUNT; i++)
    {
        pnl += random_pnl();
        if ((STOP_LIMIT < 0 && pnl <= STOP_LIMIT) || (STOP_LIMIT > 0 && pnl >= STOP_LIMIT))
        {
            // printf("Stop at %lu times\n", i);
            break;
        }
    }

    return pnl;
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));

    int total_pnl = 0;
    for (size_t i = 0; i < TEST_COUNT; i++)
    {
        total_pnl += trade();
    }

    printf("Test count: %d, trade count: %d, total pnl: %d, average pnl: %f\n", TEST_COUNT, TRADE_COUNT, total_pnl, (float)total_pnl / TEST_COUNT);

    return 0;
}
