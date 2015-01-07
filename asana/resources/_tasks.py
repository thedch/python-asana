# This file is automatically generated by generate.py using api.json

class _Tasks:
    def __init__(self, client=None):
        self.client = client

    def add_followers(self, task_id, params={}, **options):
        path = '/tasks/%d/addFollowers' % (task_id)
        return self.client.post(path, params, **options)

    def find_by_tag(self, tag_id, params={}, **options):
        path = '/tags/%d/tasks' % (tag_id)
        return self.client.get(path, params, **options)

    def find_by_tag_iterator(self, tag_id, params={}, **options):
        path = '/tags/%d/tasks' % (tag_id)
        return self.client.get_iterator(path, params, **options)

    def tags(self, task_id, params={}, **options):
        path = '/tasks/%d/tags' % (task_id)
        return self.client.get(path, params, **options)

    def tags_iterator(self, task_id, params={}, **options):
        path = '/tasks/%d/tags' % (task_id)
        return self.client.get_iterator(path, params, **options)

    def add_project(self, task_id, params={}, **options):
        path = '/tasks/%d/addProject' % (task_id)
        return self.client.post(path, params, **options)

    def create(self, params={}, **options):
        return self.client.post('/tasks', params, **options)

    def remove_tag(self, task_id, params={}, **options):
        path = '/tasks/%d/removeTag' % (task_id)
        return self.client.post(path, params, **options)

    def update(self, task_id, params={}, **options):
        path = '/tasks/%d' % (task_id)
        return self.client.put(path, params, **options)

    def find_by_project(self, project_id, params={}, **options):
        path = '/projects/%d/tasks' % (project_id)
        return self.client.get(path, params, **options)

    def find_by_project_iterator(self, project_id, params={}, **options):
        path = '/projects/%d/tasks' % (project_id)
        return self.client.get_iterator(path, params, **options)

    def find_by_id(self, task_id, params={}, **options):
        path = '/tasks/%d' % (task_id)
        return self.client.get(path, params, **options)

    def subtasks(self, task_id, params={}, **options):
        path = '/tasks/%d/subtasks' % (task_id)
        return self.client.get(path, params, **options)

    def subtasks_iterator(self, task_id, params={}, **options):
        path = '/tasks/%d/subtasks' % (task_id)
        return self.client.get_iterator(path, params, **options)

    def add_subtask(self, task_id, params={}, **options):
        path = '/tasks/%d/subtasks' % (task_id)
        return self.client.post(path, params, **options)

    def add_tag(self, task_id, params={}, **options):
        path = '/tasks/%d/addTag' % (task_id)
        return self.client.post(path, params, **options)

    def remove_followers(self, task_id, params={}, **options):
        path = '/tasks/%d/removeFollowers' % (task_id)
        return self.client.post(path, params, **options)

    def find_all(self, params={}, **options):
        return self.client.get('/tasks', params, **options)

    def find_all_iterator(self, params={}, **options):
        return self.client.get_iterator('/tasks', params, **options)

    def create_in_workspace(self, workspace_id, params={}, **options):
        path = '/workspaces/%d/tasks' % (workspace_id)
        return self.client.post(path, params, **options)

    def remove_project(self, task_id, params={}, **options):
        path = '/tasks/%d/removeProject' % (task_id)
        return self.client.post(path, params, **options)

    def set_parent(self, task_id, params={}, **options):
        path = '/tasks/%d/setParent' % (task_id)
        return self.client.post(path, params, **options)

    def projects(self, task_id, params={}, **options):
        path = '/tasks/%d/projects' % (task_id)
        return self.client.get(path, params, **options)

    def projects_iterator(self, task_id, params={}, **options):
        path = '/tasks/%d/projects' % (task_id)
        return self.client.get_iterator(path, params, **options)

    def delete(self, task_id, params={}, **options):
        path = '/tasks/%d' % (task_id)
        return self.client.delete(path, params, **options)