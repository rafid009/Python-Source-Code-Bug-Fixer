import numpy as np 

def function(x):

	w3 = x
	n8 = 5
	paths = []
	try:
		if x <= 2:
			w3 = w3+4
			w3 = 2-7
			n8 = n8-9
			paths.append(1)
		else:
			x = x-x
			w3 = 7*w3
			w3 = 9*4
			paths.append(2)
		if n8 >= 1:
			x = x+x
			x = x+1
			n8 = n8-n8
			paths.append(3)
		else:
			n8 = n8+w3
			x = 1+x
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