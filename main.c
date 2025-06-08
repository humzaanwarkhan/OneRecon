#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "recon.h"

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <domain> (use domain name)\n", argv[0]);
        return 1;
    }

    char *domain = argv[1];

    printf("=====================================\n");
    printf("          OneRecon v1.0             \n");
    printf("     Developed by Humza Anwar Khan   \n");
    printf("=====================================\n\n");

    printf("Target: %s\n\n", domain);

    printf("Select which recon steps to run:\n");
    printf("1. WHOIS\n");
    printf("2. NSLOOKUP\n");
    printf("3. PING\n");
    printf("4. SUBFINDER\n");
    printf("Enter options separated by commas (e.g., 1,3,4): ");


    char input[100];
    fgets(input, sizeof(input), stdin);

    input[strcspn(input, "\n")] = 0;

    char *token = strtok(input, ",");
    while (token != NULL) {
        int choice = atoi(token);
        switch (choice) {
            case 1: run_whois(domain); break;
            case 2: run_nslookup(domain); break;
            case 3: run_ping(domain); break;
            case 4: run_subfinder(domain); break;
            default: printf("Invalid option: %d\n", choice); break;
        }
        token = strtok(NULL, ",");
    }

    printf("\n[+] Recon finished. Output saved in the Output directory.\n");
    return 0;
}
