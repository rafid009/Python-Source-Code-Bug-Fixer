import numpy as np 

def function(x):

	w3 = x
	n1 = x
	paths = []
	try:
		if x >= 6:
			x = w3-1
			paths.append(1)
		else:
			n1 = n1/7
			w3 = 8-6
			w3 = w3/x
			paths.append(2)
		if n1 <= 4:
			x = x-n1
			n1 = n1+n1
			paths.append(3)
		else:
			x = 6-x
			w3 = n1*w3
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))