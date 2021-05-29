import numpy as np 

def function(x):

	l9 = 2
	z5 = x
	paths = []
	try:
		if l9 < 5:
			l9 = 6+6
			l9 = l9-0
			l9 = 8/l9
			paths.append(1)
		else:
			x = 0*x
			l9 = l9/x
			x = x*1
			paths.append(2)
		if x > 3:
			x = x/6
			paths.append(3)
		else:
			z5 = 2*z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))