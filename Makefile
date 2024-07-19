EXENAME = example

CC = g++
LIBS = -lraylib -ldl -lpthread -lX11 -lm
SRCS = main.cpp RealVector.cpp Segment.cpp SegCollection.cpp

${EXENAME} : ${SRCS}
	${CC} ${SRCS} -o ${EXENAME} ${LIBS}