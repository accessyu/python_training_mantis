from sys import maxsize

class Project:

    def __init__(self, id=None, project_name=None, status=None, is_inherited=None, view_status=None, desc=None):
        self.project_name = project_name
        self.status = status
        self.is_inherited = is_inherited
        self.view_status = view_status
        self.desc = desc
        self.id = id


    def __repr__(self):
        return "%s:%s" %(self.id, self.project_name)


    def __eq__(self, other):
        return (self.project_name is None or other.project_name is None or self.project_name == other.project_name) and \
                (self.status is None or other.status is None or self.status == other.status) and \
                (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize