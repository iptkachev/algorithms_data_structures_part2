class HashTable:
	_DELETED = ""

	def __init__(self, size_m: int):
		self._size_m = size_m
		self._hash_table = [None for _ in range(self._size_m)]

	def insert(self, k: int) -> bool:
		index = self._get_hash(k)

		while True:
			if self._hash_table[index] == k:
				return False
			elif self._hash_table[index] in (None, self._DELETED):
				self._hash_table[index] = k
				return True
			else:
				index = (index + 1) % self._size_m

			if index == self._get_hash(k):
				self._rehash()
				self.insert(k)
				return True

	def get_index_by_key(self, k: int) -> int | None:
		index = self._get_hash(k)

		while True:
			if self._hash_table[index] == k:
				return index
			elif self._hash_table[index] is None:
				return None
			else:
				index = (index + 1) % self._size_m

			if index == self._get_hash(k):
				return None

	def delete(self, k: int) -> bool:
		index = self.get_index_by_key(k)
		if index is None:
			return False
		else:
			self._hash_table[index] = self._DELETED
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
	hash_table = HashTable(5)
	for k in [ord(char) for char in "HCDR"]:
		print(chr(k), k, k % 5)
		hash_table.insert(k)
		print(hash_table._hash_table)
		print(hash_table.get_index_by_key(k))
	hash_table.delete(67)
	print(hash_table._hash_table)
	print(hash_table.get_index_by_key(68) is not None)
	for k in hash_table._hash_table:
		if isinstance(k, int):
			print(chr(k), end=" ")

