

import argparse

def manage_rules():
	pass


def manage_schedules():
	parser = argparse.ArgumentParser("Manage Schedule")

	parser.add_argument("--add", help="Manually add event to schedule")
	parser.add_argument("--time", help="Start time of the recording")
	parser.add_argument("--length", help="Length of recording (in hours)")

	parser.add_argument("--remove", help="Remove an event from the schedule")
	parser.add_argument("--id", help="Event ID to remove")

	parser.add_argument("--print", help="Prints a list of scheduled events")

	args = parser.parse_args()

	if args.print:
		# Get List of events from the command center
	elif args.remove != None:
		# Tell the command center to remove the provided event ID
	elif args.add:
		# Add a new event to the schedule
		

def manage_tuners():
	pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser("Communicate with DVR")
	parser.add_argument("--rules",help="Manage DVR Rules")
	parser.add_argument("--schedule",help="Manage Schedule")
	parser.add_argument("--tuners",help="Manage Tuners")

	args = parser.parse_args()

	if args.rules:
		manage_rules()

	elif args.schedule:
		manage_schedule()

	elif args.tuners:
		manage_tuners()


