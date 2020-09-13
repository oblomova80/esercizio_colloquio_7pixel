import argparse

LIMIT = 100000

def main():
	parser = argparse.ArgumentParser(add_help=True,
                                	description='funzione per calcolare minimo intero in array dove è presente anche opposto')
	parser.add_argument('-l', '--list', help='lista interi compresi tra -100000 e 100000',  nargs="+", type=int)
	args = parser.parse_args()
	input_array = [int(i) for i in args.list if in_range(int(i))]
	result = esercizio(input_array)
	print("Il più piccolo intero presente in array dato {} dove è presente opposto è {}".format(input_array, result))

def in_range(i):
	"""
	controlla se l'intero è nel range stabilito
    """
	if int(i) not in range(-LIMIT,LIMIT):
		raise Exception("Insertito intero non nel range corretto [-{limit}, {limit}]: {value}".format(limit = LIMIT, value = str(i)))
	return True

def esercizio(array):
	"""
	Ritorna il più piccolo intero
	nell'array di cui è presente anche l'opposto,
	altrimenti restituisce 0
    """
	positive_values = [ a for a in array if a > 0]
	positive_values = sorted(positive_values)
	for x in positive_values:
		if -x in array:
			return x
	return 0


if __name__ == '__main__':
    main()
