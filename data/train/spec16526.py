import numpy as np 

def function(x):

	r6 = x
	x5 = 9
	paths = []
	try:
		if x < 7:
			r6 = 4/7
			paths.append(1)
		else:
			x5 = 0/2
			paths.append(2)
		if r6 >= 6:
			x = 1+4
			x = 5/x
			r6 = 7*r6
			paths.append(3)
		else:
			x5 = 2+3
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