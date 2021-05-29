import numpy as np 

def function(x):

	w7 = x
	b0 = x
	paths = []
	try:
		if b0 <= 3:
			b0 = b0/b0
			w7 = w7/9
			paths.append(1)
		else:
			b0 = x+w7
			b0 = b0-b0
			b0 = w7-x
			paths.append(2)
		if w7 >= 4:
			b0 = b0*w7
			w7 = w7+w7
			paths.append(3)
		else:
			b0 = 2+3
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