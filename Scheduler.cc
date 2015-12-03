#include "Scheduler.h"
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

static bool
compRate(pair<double, int>& rate1, pair<double, int> rate2)
{
	return rate1.first > rate2.first;
}

void
Scheduler::RMScheduling(TaskList& task_list)
{
	vector<pair<double, int> > rate_list;

	for (int i = 0; i < task_list.getWaitingSize(); ++i) {
		Task& temp_task = task_list.getTask(i);
		double rate = (double)temp_task.getRequestTime() / (temp_task.getDeadline() - temp_task.getStartTime());

		rate_list.push_back(make_pair(rate, i));
	}
	sort(rate_list.begin(), rate_list.end(), compRate);

	int cnt = 0;
	double prev_rate = 0.0;
	for (vector<pair<double, int> >::iterator it = rate_list.begin();
		it != rate_list.end(); ++it) {
		cnt += (prev_rate != it->first) ? 1 : 0;
		task_list.getTask(it->second).setPriority(cnt);
		prev_rate = it->first;
	}

	task_list.sortList();
}

static bool
compDeadline(pair<int, int>& deadline1, pair<int, int>& deadline2)
{
	return deadline1.first < deadline2.first;
}

void
Scheduler::EDFScheduling(TaskList& task_list)
{
	vector<pair<int, int> > deadline_list;

	for (int i = 0; i < task_list.getWaitingSize(); ++i) {
		Task& temp_task = task_list.getTask(i);

		deadline_list.push_back(make_pair(temp_task.getDeadline(), i));
	}
	sort(deadline_list.begin(), deadline_list.end(), compDeadline);

	int cnt = 0, prev_deadline = 0;
	for (vector<pair<int, int> >::iterator it = deadline_list.begin();
		it != deadline_list.end(); ++it) {
		cnt += (prev_deadline != it->first) ? 1 : 0;
		task_list.getTask(it->second).setPriority(cnt);
		prev_deadline = it->first;
	}

	task_list.sortList();
}

void
Scheduler::UserScheduling(TaskList& task_list)
{
	task_list.sortList();
}