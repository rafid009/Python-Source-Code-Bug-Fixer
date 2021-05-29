import numpy as np 

def function(x):

	w3 = 0
	n1 = x
	paths = []
	try:
		if w3 > 0:
			n1 = n1+0
			w3 = w3/x
			paths.append(1)
		else:
			w3 = w3/x
			paths.append(2)
		if x >= 1:
			w3 = 5/n1
			w3 = 0/x
			paths.append(3)
		else:
			n1 = x-6
			w3 = 9*w3
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))