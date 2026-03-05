from task import Task

def test_task_mark_complete():
    task = Task("Test Task")
    task.mark_complete()
    assert task.completed is True