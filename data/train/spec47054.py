import numpy as np 

def function(x):

	b0 = x
	w7 = x
	paths = []
	try:
		if b0 <= 6:
			w7 = 7+x
			w7 = 2-w7
			b0 = 2*b0
			paths.append(1)
		else:
			w7 = 9*8
			b0 = b0/4
			b0 = 9-8
			paths.append(2)
		if b0 >= 5:
			x = b0+9
			w7 = w7/2
			paths.append(3)
		else:
			x = 3-5
			b0 = w7+w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))