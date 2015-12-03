CC = G++

INPUTFILEREADER_OBJ = InputFileReader.o
TASKFORM_OBJ = TaskForm.o
TASK_OBJ = Task.o
TASKLIST_OBJ = TaskList.o
SCHEDULER_OBJ = Scheduler.o

HJCSS_OBJ = hjCSS_main.o

COMMON_OBJS = $(INPUTFILEREADER_OBJ) $(TASKFORM_OBJ) $(TASK_OBJ) $(TASKLIST_OBJ) $(SCHEDULER_OBJ)
OBJS = $(HJCSS_OBJ) $(COMMON_OBJS)

PRODUCT = hjCSS

TARGET = $(PRODUCT)

FLAGS = -std=c++11

.SUFFIXES = .cc .o

all: $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)

#programs

$(PRODUCT) : $(HJCSS_OBJ) $(COMMON_OBJS)
	$(CC) -o $@ $(FLAGS) $(HJCSS_OBJ) $(COMMON_OBJS)

#objects

$(INPUTFILEREADER_OBJ) : InputFileReader.h TaskForm.h
	$(CC) -c -o $@ $(FLAGS) InputFileReader.cc

$(TASKFORM_OBJ) : TaskForm.h Task.h
	$(CC) -c -o $@ $(FLAGS) TaskForm.cc

$(TASK_OBJ) : Task.h
	$(CC) -c -o $@ $(FLAGS) Task.cc

$(TASKLIST_OBJ) : TaskList.h Task.h
	$(CC) -c -o $@ $(FLAGS) TaskList.cc

$(SCHEDULER_OBJ) : Scheduler.h TaskList.h
	$(CC) -c -o $@ $(FLAGS) Scheduler.cc