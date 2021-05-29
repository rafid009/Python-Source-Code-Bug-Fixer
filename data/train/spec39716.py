import numpy as np 

def function(x):

	u0 = 9
	z7 = 3
	paths = []
	try:
		if x <= 9:
			u0 = 0/4
			z7 = x*8
			u0 = u0-1
			paths.append(1)
		else:
			u0 = 6/u0
			u0 = u0+9
			paths.append(2)
		if x > 3:
			x = 7-2
			x = 3/8
			u0 = u0/3
			paths.append(3)
		else:
			x = 0*0
			x = u0/5
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))