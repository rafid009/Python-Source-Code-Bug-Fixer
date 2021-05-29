import numpy as np 

def function(x):

	i2 = 3
	x7 = 0
	paths = []
	try:
		if x7 <= 8:
			i2 = i2+7
			x = x/9
			paths.append(1)
		else:
			x7 = i2/4
			x7 = 7/x7
			paths.append(2)
		if x <= 0:
			x7 = x7*2
			x = x7+x
			paths.append(3)
		else:
			i2 = 3-i2
			x = 7*x
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