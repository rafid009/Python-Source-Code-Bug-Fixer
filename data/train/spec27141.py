import numpy as np 

def function(x):

	u9 = 4
	z7 = x
	paths = []
	try:
		if u9 <= 7:
			u9 = u9/1
			z7 = z7*3
			z7 = x-9
			paths.append(1)
		else:
			x = 0+8
			x = 4-x
			x = 7*x
			paths.append(2)
		if x > 4:
			x = z7+x
			z7 = z7*z7
			paths.append(3)
		else:
			x = x*u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))