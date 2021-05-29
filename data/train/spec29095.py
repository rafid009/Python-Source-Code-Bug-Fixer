import numpy as np 

def function(x):

	i2 = 3
	f1 = 3
	paths = []
	try:
		if f1 > 0:
			x = 7*x
			i2 = f1/x
			paths.append(1)
		else:
			i2 = 7/f1
			paths.append(2)
		if x <= 3:
			i2 = i2*9
			paths.append(3)
		else:
			f1 = f1/3
			f1 = f1*5
			x = f1*x
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