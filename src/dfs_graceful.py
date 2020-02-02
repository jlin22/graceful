class Graph: 	
	def __init__(self, adjacency_list, ends):
		self.adjacency_list = adjacency_list
		self.graceful_labelings = []
		self.graceful_ends = set()
		self.n = len(adjacency_list)

	def end_labels(self, labels):
		return list(map(lambda i: labels[i], self.ends))

	def self.initialize_remaining_labels(set_labels, i):
		remaining_labels = []
		for j in range(self.n):
			if j not in set_labels:
				remaining_labels.append(j)
		return remaining_labels
				
	def find_all_graceful_labelings():
		i = 1
		labels = []
		set_labels = {}
		remaining_labels = {0: list(range(self.n))}

		while i != 0:
			if len(remaining_labels[i]) == 0:
				i -= 1
			elif len(labels) == self.n:
				if self.is_graceful(labels):
					end_labels = self.end_labels(labels)
					self.graceful_labelings.append(end_labels)
					self.graceful_ends.add(end_labels)
					v = labels.pop()
					set_labels.remove(v)
					i -= 1
			else:
				current_label = remaining_labels[i].pop()
				if self.is_valid_label(i, current_label, labels):
					labels.append(current_label)
					set_labels.add(current_label)
					i += 1
					self.initialize_remaining_labels(set_labels, i)
				


					

