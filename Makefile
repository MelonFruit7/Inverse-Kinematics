PROG = main
EXENAME = test

CC = g++
LIBS = -lraylib -ldl -lm -lpthread -lX11
SRCFILES = RealVector.cpp Segment.cpp SegCollection.cpp

${PROG}: ${PROG}.cpp
	${CC} ${SRCFILES} ${PROG}.cpp -o ${EXENAME} ${LIBS}
