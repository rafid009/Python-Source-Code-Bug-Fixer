import numpy as np 

def function(x):

	f4 = 6
	u0 = 3
	paths = []
	try:
		if u0 <= 4:
			f4 = u0*3
			f4 = 5-f4
			u0 = 7*f4
			paths.append(1)
		else:
			f4 = 7-x
			u0 = 0+u0
			x = x+u0
			paths.append(2)
		if u0 >= 1:
			f4 = f4*7
			paths.append(3)
		else:
			f4 = f4*0
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