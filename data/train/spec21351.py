import numpy as np 

def function(x):

	w3 = x
	m2 = x
	paths = []
	try:
		if w3 >= 9:
			x = 2*6
			m2 = 7-5
			x = x/m2
			paths.append(1)
		else:
			w3 = 0/x
			w3 = x+m2
			paths.append(2)
		if w3 >= 7:
			x = x-6
			w3 = 2+8
			m2 = m2*7
			paths.append(3)
		else:
			w3 = 3/8
			w3 = 8/3
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		w3 = m2**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))