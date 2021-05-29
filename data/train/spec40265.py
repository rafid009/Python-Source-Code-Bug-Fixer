import numpy as np 

def function(x):

	b7 = 3
	k4 = x
	paths = []
	try:
		if k4 < 2:
			k4 = 4/k4
			x = x-0
			b7 = 6+b7
			paths.append(1)
		else:
			k4 = k4+b7
			b7 = 7+b7
			paths.append(2)
		if k4 < 7:
			k4 = k4-k4
			k4 = k4+k4
			paths.append(3)
		else:
			x = x+8
			k4 = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))