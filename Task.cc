#include "Task.h"

using namespace std;

Task::Task() 
{
	taskName = "";
	startTime = 0;
	endTime = 0;
	requestTime = 0;
	progressedTime = 0;
	deadline = 0;
	priority = 0;
	done = false;
}

Task::Task
(std::string task_name, int request_time, int deadline, int priority) 
{
	taskName = task_name;
	startTime = 0;
	endTime = 0;
	requestTime = request_time;
	progressedTime = 0;
	this->deadline = deadline;
	this->priority = priority;
	done = false;
}
    
bool 
Task::doneOnTime()
{
	if (done) {
		return (endTime <= deadline) ? true : false;
	} 

	return false;
}

int 
Task::getResponseTime()
{
	return endTime - startTime + 1;
}

void 
Task::updateProgressedTime(int progressed_time)
{
	if (!done)
		progressedTime += progressed_time;

	if (progressedTime >= requestTime)
		done = true;
}
    
string 
Task::getName()
{
	return taskName;
}

bool
Task::Done()
{
	return done;
}

void 
Task::setStartTime(int start_time)
{
	startTime = start_time;
}

void 
Task::setEndTime(int end_time)
{
	endTime = end_time;
}

void
Task::setPriority(int priority)
{
	this->priority = priority;
}

int
Task::getPriority()
{
	return priority;
}

int
Task::getStartTime()
{
	return startTime;
}

int
Task::getDeadline()
{
	return deadline;
}

int
Task::getRequestTime()
{
	return requestTime;
}