#include "InputFileReader.h"
#include "TaskForm.h"
#include "Task.h"
#include "TaskList.h"
#include "Scheduler.h"
#include <iostream>

using namespace std;

static bool 
wholeTaskDone(vector<TaskVector >& tasks) {
	bool done = true;

	for (vector<TaskVector >::iterator it = tasks.begin();
		it != tasks.end(); ++it) {
		if (it->size() != 0) {
			done = false;
			break;
		}
	}

	return done;
}

static void
addTaskToWorking(TaskList& working_list, vector<TaskVector>& tasks, int cur_time) {
	for (vector<TaskVector>::iterator it = tasks.begin();
		it != tasks.end(); ++it) {
		int rm_cnt = 0;
		/* if cur_time == start_time of task, 
		   move task from reserve_vector to working list */
		for (int i = 0; i < it->size() && (*it)[i].first <= cur_time; ++i) {
			if ((*it)[i].first == cur_time) {
				Task temp = (*it)[i].second;
				working_list.pushTask(temp, cur_time);
				cout << cur_time << "\t" << temp.getName() << "\tadd." << endl;
				rm_cnt++;
			}
		}
		for (int i = 0; i < rm_cnt; ++i) it->erase(it->begin());
	}
}

int main(int argc, char* argv[])
{
	/* USAGE : ./hjCSS [Input file] [scheduling mode] 
	   scheduling mode :
	       0 : rm scheduling
	       1 : edf scheduling
	       2 : user scheduling
	*/
	if (argc != 3) return -1;
	InputFileReader reader;
	vector<TaskForm> task_forms; 
	try {
		task_forms = reader.readFile(argv[1]);
	} catch (string msg) {
		cout << msg << endl;
		return -1;
	}

	vector<TaskVector > tasks;

	/* make task lists */
	for (vector<TaskForm>::iterator it = task_forms.begin();
		it != task_forms.end(); ++it) {
		tasks.push_back(it->makeTaskList());
	}

	TaskList working_list;
	Scheduler scheduler;
	int cur_time = 0, prev_cnt = 0;
	while (!wholeTaskDone(tasks) | !working_list.everyDone()) {
		/* increase clock */
		cur_time++;
		addTaskToWorking(working_list, tasks, cur_time);
		switch(argv[2][0] - '0') {
			case 0 : scheduler.RMScheduling(working_list); break;
			case 1 : scheduler.EDFScheduling(working_list); break;
			case 2 : scheduler.UserScheduling(working_list); break;
			default : break;
		}

		if (working_list.updateTask(1, cur_time)) {
			Task& cur_task = (prev_cnt != working_list.end_list.size()) ? 
				working_list.end_list[working_list.end_list.size()-1] : working_list.getTopTask();
			cout << cur_time << "\t" << cur_task.getName();
			if (!cur_task.Done()) {
				cout << "\t" << "Running...." << endl;
			} else {
				cout << "\t" << "Done." << endl;
			}

			prev_cnt = working_list.end_list.size();
		} else {
			cout << cur_time << "\tCPU waiting..." << endl;
		}
	}

	return 0;
}