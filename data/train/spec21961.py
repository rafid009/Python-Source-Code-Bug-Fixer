import numpy as np 

def function(x):

	n8 = x
	w7 = x
	paths = []
	try:
		if n8 > 4:
			x = x+1
			n8 = 3-n8
			paths.append(1)
		else:
			w7 = w7+8
			n8 = n8/2
			paths.append(2)
		if x >= 1:
			n8 = w7+n8
			w7 = w7*7
			paths.append(3)
		else:
			n8 = n8+2
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))