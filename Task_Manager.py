checklist = []
n = int(input("Enter number of tasks for today: "))

for i in range(n):
    task = input(f"Enter task {i+1}: ")
    checklist.append(task)

completed_tasks = []
incomplete_tasks = []

print("\nReview your tasks:")
for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ").lower()
    
    if status == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\n--- Daily Task Summary ---")
print("Completed Tasks:", completed_tasks)
print("Incomplete Tasks:", incomplete_tasks)
