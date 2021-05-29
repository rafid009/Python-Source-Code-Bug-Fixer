import numpy as np 

def function(x):

	j3 = 2
	b0 = x
	paths = []
	try:
		if x >= 5:
			j3 = j3+0
			paths.append(1)
		else:
			b0 = b0*x
			x = 3/x
			paths.append(2)
		if b0 >= 2:
			x = 8*1
			b0 = b0+6
			paths.append(3)
		else:
			b0 = b0/2
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