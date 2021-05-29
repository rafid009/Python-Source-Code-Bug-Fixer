import numpy as np 

def function(x):

	u5 = x
	i0 = 7
	paths = []
	try:
		if i0 > 7:
			u5 = x-u5
			paths.append(1)
		else:
			u5 = 8*u5
			i0 = x-i0
			i0 = 9*7
			paths.append(2)
		if x >= 7:
			x = x-8
			u5 = 0+u5
			paths.append(3)
		else:
			u5 = u5+0
			u5 = u5+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))