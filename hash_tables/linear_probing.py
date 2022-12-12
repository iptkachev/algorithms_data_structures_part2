class HashTable:
	def __init__(self, size_m: int):
		self._size_m = size_m
		self._hash_table = [None for _ in range(self._size_m)]

	def get_index_by_key(self, k: int) -> int | None:
		index = self._get_hash(k)
		while True:
			if self._hash_table[index] == k:
				return index
			index += 1

			if index == self._get_hash(k):
				return None

	def insert(self, k: int) -> bool:
		index = self._get_hash(k)

		while True:
			if self._hash_table[index] == k:
				return False
			elif self._hash_table[index] is None:
				self._hash_table[index] = k
				return True
			else:
				index = (index + 1) % self._size_m

			if index == self._get_hash(k):
				self._rehash()
				self.insert(k)
				return True

	def _get_hash(self, k: int) -> int:
		return k % self._size_m

	def _rehash(self):
		new_hash_table = HashTable(self._size_m * 2)
		for k in self._hash_table:
			new_hash_table.insert(k)
		self._hash_table = new_hash_table._hash_table
		self._size_m = self._size_m


if __name__ == "__main__":
	hash_table = HashTable(7)
	for k in [33, 77, 708, 49]:
		hash_table.insert(k)
		print(hash_table._hash_table)
		print(hash_table.get_index_by_key(k))