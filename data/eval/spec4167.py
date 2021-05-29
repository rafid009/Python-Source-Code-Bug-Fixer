import numpy as np 

def function(x):

	f6 = x
	u0 = x
	paths = []
	try:
		if u0 >= 4:
			u0 = 3*7
			paths.append(1)
		else:
			f6 = 1*f6
			u0 = u0-5
			paths.append(2)
		if x <= 9:
			x = 1/4
			f6 = f6/u0
			x = f6/x
			paths.append(3)
		else:
			f6 = f6*0
			u0 = f6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))