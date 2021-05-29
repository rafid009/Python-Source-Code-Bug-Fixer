import numpy as np 

def function(x):

	h8 = 7
	l1 = 7
	paths = []
	try:
		if l1 <= 0:
			l1 = l1*l1
			h8 = 2*h8
			paths.append(1)
		else:
			h8 = x/5
			l1 = 6-l1
			paths.append(2)
		if x <= 3:
			x = 1+x
			paths.append(3)
		else:
			l1 = l1+h8
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