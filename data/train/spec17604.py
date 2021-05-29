import numpy as np 

def function(x):

	i2 = x
	f2 = x
	paths = []
	try:
		if x >= 3:
			x = 9-8
			x = 7+f2
			paths.append(1)
		else:
			f2 = f2/f2
			x = x/9
			x = 7*x
			paths.append(2)
		if f2 <= 6:
			f2 = 1*f2
			paths.append(3)
		else:
			i2 = i2/x
			i2 = f2-9
			i2 = i2-5
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