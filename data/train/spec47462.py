import numpy as np 

def function(x):

	v7 = x
	i2 = x
	paths = []
	try:
		if x >= 8:
			x = x*3
			v7 = 3*v7
			paths.append(1)
		else:
			x = v7*x
			i2 = 8/i2
			i2 = 8-i2
			paths.append(2)
		if i2 < 7:
			i2 = v7+i2
			paths.append(3)
		else:
			x = v7-4
			i2 = 3+i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))