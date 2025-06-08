// recon.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "recon.h"

void run_whois(char *domain) {
    printf("[+] Running WHOIS...\n");
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "whois %s > output/%s_whois.txt", domain, domain);
    system(cmd);
}

void run_nslookup(char *domain) {
    printf("[+] Running NSLOOKUP...\n");
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "nslookup %s > output/%s_nslookup.txt", domain, domain);
    system(cmd);
}

void run_ping(char *domain) {
    printf("[+] Running PING test...\n");
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "ping -c 4 %s > output/%s_ping.txt", domain, domain);
    system(cmd);
}

void run_subfinder(char *domain) {
    printf("[+] Running subdfinder...\n");
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "subfinder -d %s -o output/%s_subdomains.txt", domain, domain);
    system(cmd);
}

