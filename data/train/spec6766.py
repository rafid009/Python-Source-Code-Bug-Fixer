import numpy as np 

def function(x):

	w2 = 0
	n3 = 8
	paths = []
	try:
		if x >= 3:
			w2 = 7+w2
			w2 = 2*w2
			x = 5/w2
			paths.append(1)
		else:
			n3 = 9+0
			paths.append(2)
		if x < 3:
			x = x/2
			n3 = x/8
			n3 = 7+n3
			paths.append(3)
		else:
			n3 = n3+x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))