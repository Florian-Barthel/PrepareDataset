
class Pipeline:
    def __init__(self, task_list):
        self.task_list = task_list

    def run(self):
        for i, task in enumerate(self.task_list):
            print('Task {} of {}'.format(i + 1, len(self.task_list)))
            task.run()
            task.print_summary()
