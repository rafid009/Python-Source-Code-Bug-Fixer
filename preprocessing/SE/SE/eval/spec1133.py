import numpy as np 

def function(x):

	f3 = x
	f7 = x
	paths = []
	try:
		if f7 < 8:
			f7 = 4*1
			f3 = f3-x
			f7 = f7+f3
			paths.append(1)
		else:
			x = x*f3
			x = 6/f3
			paths.append(2)
		if f3 < 9:
			f7 = f3/1
			f3 = f3*9
			paths.append(3)
		else:
			f7 = f7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))