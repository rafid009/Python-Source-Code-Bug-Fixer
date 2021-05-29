import numpy as np 

def function(x):

	u5 = 2
	f1 = 6
	paths = []
	try:
		if u5 >= 0:
			f1 = u5-x
			u5 = f1*f1
			paths.append(1)
		else:
			x = 1+u5
			f1 = f1*u5
			u5 = u5+f1
			paths.append(2)
		if f1 >= 3:
			f1 = f1-0
			f1 = 2+u5
			x = f1*x
			paths.append(3)
		else:
			u5 = x-4
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