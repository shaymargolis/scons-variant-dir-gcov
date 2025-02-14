#ifdef CONFIG_A

int main(int argc, char const *argv[])
{
    printf("A\n");
    return 0;
}

#elif CONFIG_B

int main(int argc, char const *argv[])
{
    printf("B\n");
    return 0;
}

#elif CONFIG_C

int main(int argc, char const *argv[])
{
    printf("C\n");
    return 0;
}

#endif
