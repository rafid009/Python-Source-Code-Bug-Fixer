import numpy as np 

def function(x):

	e7 = 4
	i2 = 7
	paths = []
	try:
		if x < 6:
			e7 = e7-e7
			x = 6+7
			i2 = 1+i2
			paths.append(1)
		else:
			e7 = 6*e7
			e7 = e7*4
			e7 = 7*i2
			paths.append(2)
		if x >= 9:
			x = x+2
			x = 4-x
			paths.append(3)
		else:
			i2 = x-i2
			e7 = i2-2
			e7 = 5-e7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))