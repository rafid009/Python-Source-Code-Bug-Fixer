import numpy as np 

def function(x):

	b0 = x
	o2 = 7
	paths = []
	try:
		if x < 0:
			x = 5/x
			paths.append(1)
		else:
			x = 3/x
			x = 9+x
			paths.append(2)
		if x >= 1:
			x = 5*x
			b0 = b0+4
			o2 = 5+b0
			paths.append(3)
		else:
			b0 = b0/2
			o2 = 0/5
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		o2 = b0**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))