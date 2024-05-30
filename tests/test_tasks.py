from task_manager.tasks import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("Test Task")
    assert "Test Task" in manager.tasks

def test_list_tasks():
    manager = TaskManager()
    manager.add_task("Test Task")
    assert len(manager.tasks) == 1

def test_delete_task():
    manager = TaskManager()
    manager.add_task("Test Task")
    manager.delete_task("Test Task")
    assert "Test Task" not in manager.tasks
