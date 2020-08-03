import hashlib

#define the function concatenate and hash
def hash_ab(tx1,tx2):
	tx12_hash = hashlib.sha256(tx1).hexdigest() +  hashlib.sha256(tx2).hexdigest()
	return hashlib.sha256(tx12_hash).hexdigest()

#define the merkle tree function
def txab_hash(hash_list):
	hash_ab_list=[]

	for index in range(0, len(hash_list), 2):

		if index + 1 != len(hash_list):
			tx_b = hash_list[index + 1]
		else:

			#if no more element left, use itself again
			tx_b = tx_a
		tx_a = hash_list[index]

		hash_ab_list.append(hash_ab(tx_a,tx_b))
	return hash_ab_list


if __name__ == "__main__":

	# input the transactions"
	transaction = ["ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
    "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
    "2e7d2c03a9507ae265ecf5b5356885a53393a2929d241394997265a1a25aefc6",
    "18ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4",
	"3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea"]

	print transaction
	while len(transaction) > 1:
		transaction = txab_hash(transaction)
		print '-'*100
		print transaction