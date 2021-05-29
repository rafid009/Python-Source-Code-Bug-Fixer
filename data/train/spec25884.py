import numpy as np 

def function(x):

	f6 = 2
	z5 = 2
	paths = []
	try:
		if z5 <= 3:
			f6 = 3*z5
			f6 = 5*f6
			paths.append(1)
		else:
			z5 = 0-z5
			x = f6/f6
			z5 = z5*2
			paths.append(2)
		if x > 2:
			x = z5+x
			x = 2/8
			paths.append(3)
		else:
			z5 = z5+f6
			x = f6+1
			z5 = 8-z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		f6 = z5**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))