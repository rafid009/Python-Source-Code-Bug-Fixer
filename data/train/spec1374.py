import numpy as np 

def function(x):

	u9 = x
	z8 = x
	paths = []
	try:
		if u9 <= 4:
			x = 9*x
			paths.append(1)
		else:
			u9 = 0*u9
			z8 = 9/z8
			paths.append(2)
		if u9 < 7:
			u9 = 5*u9
			x = x*8
			x = 3-x
			paths.append(3)
		else:
			z8 = 7/5
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))