import numpy as np 

def function(x):

	l9 = x
	r4 = x
	paths = []
	try:
		if r4 > 6:
			x = x*6
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x > 3:
			x = x-4
			x = x-9
			l9 = l9+9
			paths.append(3)
		else:
			x = 0*x
			l9 = l9-x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))