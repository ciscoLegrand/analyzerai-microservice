from collections import defaultdict, Counter

class FrequentlyWord:
    def __init__(self, data):
        self.enterprise_id = data.get('enterprise_id', '')
        self.year = data.get('year', '')
        self.quarter = data.get('quarter', '')
        self.word_counts = data.get('word_counts', Counter())
        self.frequency_comments = data.get('frequency_comments', defaultdict(int))
        self.frequency_employees = data.get('frequency_employees', defaultdict(set))
        self.total_comments = data.get('total_comments', 0)
        self.unique_employee_ids = data.get('unique_employee_ids', set())
        self.total_answers = data.get('total_answers', 0)
        self.commenting_employees = data.get('commenting_employees', set())

