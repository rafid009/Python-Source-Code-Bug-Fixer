import numpy as np 

def function(x):

	r8 = 8
	u5 = 2
	paths = []
	try:
		if r8 <= 8:
			r8 = 1*r8
			u5 = u5*5
			u5 = 8+7
			paths.append(1)
		else:
			r8 = x/r8
			paths.append(2)
		if x < 7:
			u5 = 9+r8
			x = x*4
			u5 = r8-9
			paths.append(3)
		else:
			r8 = 6*6
			r8 = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))