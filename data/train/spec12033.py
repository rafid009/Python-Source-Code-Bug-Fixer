import numpy as np 

def function(x):

	r4 = 5
	u5 = 9
	paths = []
	try:
		if x < 5:
			r4 = x-r4
			x = x+1
			paths.append(1)
		else:
			u5 = u5+1
			paths.append(2)
		if r4 <= 0:
			u5 = 5-x
			x = x-9
			x = u5*x
			paths.append(3)
		else:
			x = r4*u5
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