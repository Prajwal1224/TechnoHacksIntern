class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')

    def show_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
