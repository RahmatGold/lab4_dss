# Authors: Rahmatulloh and Bahodir
# 6.1 Without them == compares identity and hash comes from the address, so every object is different.
# 6.2 If only __eq__ is defined, Python sets __hash__ to None, so the object is unhashable.
# 6.3 Same student = same student_id (a group change is still the same person).
# 6.4 If hash uses group and the group changes, "s in seen" is False (the set looks in the wrong place).
# 6.5 frozen dataclass compares all fields, so a student with a new group would be a different one, and the group can not be changed.
class Student:
    def __init__(self, student_id, full_name, group):
        self.student_id = student_id
        self.full_name = full_name
        self.group = group
    def __eq__(self, other):
        return isinstance(other, Student) and self.student_id == other.student_id
    def __hash__(self):
        return hash(self.student_id)
    def __repr__(self):
        return f"Student(student_id={self.student_id!r}, group={self.group!r})"

def test_student():
    seen = set()
    for row in [("U2310045", "Ali Valiyev", "SE-31")] * 2:
        seen.add(Student(*row))
    assert len(seen) == 1
    s = Student("U2310045", "Ali Valiyev", "SE-31")
    s.group = "SE-32"
    assert s in seen
    assert repr(s) == "Student(student_id='U2310045', group='SE-32')"


