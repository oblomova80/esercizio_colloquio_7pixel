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
