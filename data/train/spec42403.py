import numpy as np 

def function(x):

	r2 = x
	u5 = 2
	paths = []
	try:
		if u5 >= 8:
			u5 = 9/u5
			u5 = 3*u5
			paths.append(1)
		else:
			r2 = r2+7
			x = x+5
			u5 = r2/1
			paths.append(2)
		if x < 9:
			x = x/7
			paths.append(3)
		else:
			r2 = 0*r2
			x = 6-0
			r2 = r2/4
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