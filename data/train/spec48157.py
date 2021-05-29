import numpy as np 

def function(x):

	q3 = 2
	i2 = x
	paths = []
	try:
		if q3 <= 0:
			q3 = 3+q3
			paths.append(1)
		else:
			i2 = x/i2
			i2 = x/8
			i2 = i2-i2
			paths.append(2)
		if q3 >= 2:
			x = i2-2
			paths.append(3)
		else:
			q3 = q3/3
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