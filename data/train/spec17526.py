import numpy as np 

def function(x):

	i2 = 7
	j6 = 3
	paths = []
	try:
		if j6 >= 8:
			i2 = 2*i2
			paths.append(1)
		else:
			i2 = 2+i2
			paths.append(2)
		if i2 > 6:
			i2 = 8/i2
			i2 = i2*5
			x = 7-x
			paths.append(3)
		else:
			j6 = 9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))