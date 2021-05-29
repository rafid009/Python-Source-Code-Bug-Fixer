import numpy as np 

def function(x):

	e7 = x
	i2 = 3
	paths = []
	try:
		if x < 0:
			e7 = e7*e7
			e7 = e7+e7
			paths.append(1)
		else:
			e7 = i2-5
			paths.append(2)
		if i2 >= 3:
			i2 = i2-3
			i2 = 2-i2
			i2 = i2-8
			paths.append(3)
		else:
			i2 = x+i2
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		i2 = e7**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))