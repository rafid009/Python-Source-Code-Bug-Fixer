import numpy as np 

def function(x):

	y3 = x
	f4 = x
	paths = []
	try:
		if f4 < 0:
			y3 = x/x
			f4 = f4-2
			paths.append(1)
		else:
			y3 = y3/4
			x = 7+f4
			f4 = f4-9
			paths.append(2)
		if f4 < 3:
			y3 = x/9
			y3 = 3-x
			paths.append(3)
		else:
			f4 = 5/8
			f4 = f4/5
			f4 = 6*f4
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