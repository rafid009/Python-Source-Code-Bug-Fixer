import numpy as np 

def function(x):

	n5 = 7
	w2 = x
	paths = []
	try:
		if x <= 0:
			n5 = 6*w2
			paths.append(1)
		else:
			w2 = w2/9
			w2 = w2*x
			n5 = 7/6
			paths.append(2)
		if x <= 2:
			n5 = n5+n5
			paths.append(3)
		else:
			w2 = 6+5
			x = w2*x
			w2 = 8-3
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))