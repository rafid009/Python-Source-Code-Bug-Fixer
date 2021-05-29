import numpy as np 

def function(x):

	r8 = 7
	u5 = 7
	paths = []
	try:
		if r8 > 9:
			r8 = 2+7
			x = x*r8
			paths.append(1)
		else:
			r8 = 2*x
			r8 = 0-x
			u5 = 7-u5
			paths.append(2)
		if u5 < 6:
			r8 = 1+3
			x = 9/x
			paths.append(3)
		else:
			r8 = 0+2
			r8 = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))