from model.project import Project
import random

def test_add_project(app):
    project = Project(project_name='new name', status='development', is_inherited=True,
                      view_status='private', desc='TEST desc')
    project_list_old = app.soap.get_project_list()
    if project in project_list_old:
        app.project.delete_project(project)
        project_list_old = app.soap.get_project_list()
    app.project.create_project(project)
    project_list_new = app.project.get_project_list()
    project_list_old.append(project)
    assert sorted(project_list_old, key=Project.id_or_max) == sorted(project_list_new, key=Project.id_or_max)

def test_del_project(app):
    project_list_old = app.soap.get_project_list()
    if len(project_list_old) == 0:
        project = Project(project_name='new name', status='development', is_inherited=True,
                          view_status='private', desc='TEST desc')
        app.project.create_project(project)
    chosen_project = random.choice(project_list_old)
    app.project.delete_project(chosen_project)
    project_list_new = app.soap.get_project_list()
    project_list_old.remove(chosen_project)
    assert sorted(project_list_old, key=Project.id_or_max) == sorted(project_list_new, key=Project.id_or_max)

