import numpy as np 

def function(x):

	n8 = 0
	w5 = 4
	paths = []
	try:
		if w5 < 4:
			n8 = n8+1
			n8 = n8+2
			paths.append(1)
		else:
			n8 = n8+n8
			paths.append(2)
		if x < 1:
			n8 = n8*w5
			x = x+9
			paths.append(3)
		else:
			w5 = w5*x
			w5 = 4+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))