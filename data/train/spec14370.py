import numpy as np 

def function(x):

	u5 = x
	a5 = x
	paths = []
	try:
		if x <= 0:
			a5 = 8+a5
			a5 = a5*a5
			u5 = u5*9
			paths.append(1)
		else:
			x = 2/u5
			u5 = 1-u5
			a5 = a5*4
			paths.append(2)
		if x <= 1:
			x = x+1
			u5 = u5-6
			a5 = a5*a5
			paths.append(3)
		else:
			a5 = x*4
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))