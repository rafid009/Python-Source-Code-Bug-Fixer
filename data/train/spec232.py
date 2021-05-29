import numpy as np 

def function(x):

	w3 = x
	k1 = x
	paths = []
	try:
		if x <= 9:
			w3 = w3*k1
			paths.append(1)
		else:
			w3 = w3+x
			x = w3-w3
			paths.append(2)
		if k1 >= 7:
			k1 = 3*3
			paths.append(3)
		else:
			w3 = 8*8
			w3 = 5-0
			w3 = 2-w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))