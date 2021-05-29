import numpy as np 

def function(x):

	f5 = 2
	i2 = x
	paths = []
	try:
		if x > 8:
			f5 = f5/7
			f5 = f5-9
			i2 = 8-2
			paths.append(1)
		else:
			i2 = 2*i2
			paths.append(2)
		if x >= 3:
			f5 = 2*i2
			i2 = i2-7
			f5 = 1-f5
			paths.append(3)
		else:
			x = 4/x
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))