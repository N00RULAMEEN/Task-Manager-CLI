from project import Add_TO_DO, Del_TO_DO, mark_done, filter_tasks


def test_add():
    tasks = {}

    tasks = Add_TO_DO(tasks, "High", "Test Task", "2026-01-01")

    assert len(tasks) == 1

    day = list(tasks.keys())[0]
    task = tasks[day][0]

    assert task["title"] == "Test Task"
    assert task["priority"] == "High"
    assert task["done"] == False


def test_delete():
    tasks = {}

    tasks = Add_TO_DO(tasks, "High", "Task1", "2026-01-01")
    tasks = Add_TO_DO(tasks, "Low", "Task2", "2026-01-02")

    day = list(tasks.keys())[0]
    task_id = tasks[day][0]["id"]

    tasks, found = Del_TO_DO(tasks, task_id)

    assert found == True


def test_done():
    tasks = {}

    tasks = Add_TO_DO(tasks, "High", "Task1", "2026-01-01")

    day = list(tasks.keys())[0]
    task_id = tasks[day][0]["id"]

    tasks, found = mark_done(tasks, task_id)

    assert found == True
    assert tasks[day][0]["done"] == True


def test_pending_filter():
    tasks = {}

    tasks = Add_TO_DO(tasks, "High", "Task1", "2026-01-01")

    day = list(tasks.keys())[0]
    task_id = tasks[day][0]["id"]

    tasks, _ = mark_done(tasks, task_id)

    pending = filter_tasks(tasks, "pending")

    assert pending == {}