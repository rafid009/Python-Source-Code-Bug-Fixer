import numpy as np 

def function(x):

	b1 = 3
	a6 = x
	paths = []
	try:
		if x < 6:
			b1 = b1+b1
			paths.append(1)
		else:
			b1 = 0/5
			paths.append(2)
		if a6 >= 3:
			b1 = 3+4
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))