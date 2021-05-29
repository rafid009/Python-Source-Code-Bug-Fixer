import numpy as np 

def function(x):

	b2 = x
	w5 = 7
	paths = []
	try:
		if w5 >= 4:
			b2 = 5*x
			paths.append(1)
		else:
			x = 8-7
			x = 3+b2
			paths.append(2)
		if x > 1:
			b2 = b2-x
			w5 = x-w5
			w5 = w5-w5
			paths.append(3)
		else:
			w5 = 9/3
			x = 4*x
			b2 = w5+b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))