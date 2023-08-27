from collections import defaultdict, Counter

class WordFrequency:
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

    def word_frequency_ratio(self):
        """Returns the ratio of word frequency to total comments."""
        return self.frequency_word / self.total_comments if self.total_comments != 0 else 0

    def employee_commenting_ratio(self):
        """Returns the ratio of employees commenting to total employees."""
        return self.total_employees_commenting / self.total_employees if self.total_employees != 0 else 0
