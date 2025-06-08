CC = gcc
CFLAGS = -Wall

all: OneRecon

OneRecon: main.o recon.o
	$(CC) $(CFLAGS) -o OneRecon main.o recon.o

main.o: main.c recon.h
	$(CC) $(CFLAGS) -c main.c

recon.o: recon.c recon.h
	$(CC) $(CFLAGS) -c recon.c

clean:
	rm -f *.o OneRecon
