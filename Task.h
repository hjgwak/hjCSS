#ifndef __TASK_H__
#define __TASK_H__

#include <string>

class Task {
	public:
    	Task();
    	Task(std::string task_name, int request_time, int deadline, int priority = 1);
    
    	void updateProgressedTime(int progressed_time);
    	
    	void setStartTime(int start_time);
    	void setEndTime(int end_time);
    	void setPriority(int priority);

    	bool doneOnTime();
		int getResponseTime();
		std::string getName();
		bool Done();
		int getPriority();
        int getStartTime();
        int getDeadline();
        int getRequestTime();

	private:
    	std::string taskName;
    	int startTime;
    	int endTime;
    	int requestTime;
    	int progressedTime;
    	int deadline;
    	int priority;
    	bool done;
};

#endif //__TASK_H__