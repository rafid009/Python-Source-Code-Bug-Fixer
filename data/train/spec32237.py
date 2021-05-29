import numpy as np 

def function(x):

	h2 = x
	w3 = x
	paths = []
	try:
		if h2 < 8:
			h2 = x*4
			paths.append(1)
		else:
			x = x*9
			x = 4+9
			h2 = 8+h2
			paths.append(2)
		if x >= 8:
			x = x/2
			paths.append(3)
		else:
			h2 = x+x
			w3 = w3/7
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))