import numpy as np 

def function(x):

	e7 = 4
	i2 = x
	paths = []
	try:
		if e7 <= 0:
			x = e7-5
			e7 = 7-e7
			paths.append(1)
		else:
			i2 = i2+0
			i2 = i2+7
			i2 = i2*e7
			paths.append(2)
		if i2 >= 4:
			x = 5-4
			i2 = 1/8
			i2 = i2+7
			paths.append(3)
		else:
			i2 = 4-1
			i2 = e7+x
			i2 = x/e7
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