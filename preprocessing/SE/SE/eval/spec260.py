import numpy as np 

def function(x):

	l9 = 3
	k0 = 3
	paths = []
	try:
		if x <= 0:
			l9 = 3*k0
			paths.append(1)
		else:
			l9 = l9+9
			x = 3-6
			paths.append(2)
		if x >= 9:
			x = x-4
			paths.append(3)
		else:
			l9 = x+4
			k0 = 0*2
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