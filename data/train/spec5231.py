import numpy as np 

def function(x):

	k3 = x
	x9 = x
	paths = []
	try:
		if x <= 0:
			x = x+9
			x = 2+x9
			x9 = x*x9
			paths.append(1)
		else:
			k3 = x+x9
			x = x+2
			x9 = x9*4
			paths.append(2)
		if x9 > 9:
			x9 = 3*x9
			x9 = x/x9
			k3 = x9/5
			paths.append(3)
		else:
			k3 = 8+3
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))