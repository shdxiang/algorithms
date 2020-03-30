#include <stdlib.h>
#include <stdio.h>
#include <time.h>

static int TEST_COUNT = 0;
static int TRADE_COUNT = 0;
static int STOP_LIMIT = -0;

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
    if (argc != 4)
    {
        printf("Usage: %s <TEST_COUNT> <TRADE_COUNT> <STOP_LIMIT>\n", argv[0]);
        return -1;
    }

    TEST_COUNT = atoi(argv[1]);
    TRADE_COUNT = atoi(argv[2]);
    STOP_LIMIT = atoi(argv[3]);

    printf("Number of tests: %d\n", TEST_COUNT);
    printf("Trades in each test: %d\n", TRADE_COUNT);
    printf("Stop limit: %d\n", STOP_LIMIT);

    printf("Trading\n");

    srand(time(NULL));

    float total_pnl = 0;
    for (size_t i = 0; i < TEST_COUNT; i++)
    {
        total_pnl += trade();
    }

    printf("Total PNL: %f\n", total_pnl);
    printf("Average PNL: %f\n", total_pnl / TEST_COUNT);

    return 0;
}
