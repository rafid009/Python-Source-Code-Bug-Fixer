import numpy as np 

def function(x):

	n4 = 6
	w2 = 3
	paths = []
	try:
		if w2 > 2:
			x = 5*x
			w2 = w2*7
			w2 = w2*1
			paths.append(1)
		else:
			w2 = w2-x
			n4 = w2/x
			paths.append(2)
		if x >= 2:
			n4 = 0/n4
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))