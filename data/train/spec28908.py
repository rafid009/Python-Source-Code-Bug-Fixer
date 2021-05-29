import numpy as np 

def function(x):

	y3 = 4
	f4 = x
	paths = []
	try:
		if f4 > 8:
			y3 = y3/y3
			f4 = f4+x
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if y3 > 2:
			x = x+3
			x = 4+f4
			paths.append(3)
		else:
			x = x/y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))