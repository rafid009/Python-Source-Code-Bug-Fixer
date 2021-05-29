import numpy as np 

def function(x):

	f4 = 5
	z7 = x
	paths = []
	try:
		if z7 < 4:
			x = x+x
			paths.append(1)
		else:
			x = 1*6
			z7 = 2+z7
			x = x*x
			paths.append(2)
		if z7 < 4:
			x = f4/f4
			x = 1+8
			z7 = x*z7
			paths.append(3)
		else:
			f4 = 0-3
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))