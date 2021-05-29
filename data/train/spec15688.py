import numpy as np 

def function(x):

	s7 = x
	i2 = 7
	paths = []
	try:
		if x >= 1:
			i2 = i2*3
			x = x*6
			paths.append(1)
		else:
			x = i2*s7
			x = x+1
			paths.append(2)
		if x <= 3:
			x = x+x
			x = 5/x
			paths.append(3)
		else:
			x = x-1
			x = 2+x
			i2 = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))