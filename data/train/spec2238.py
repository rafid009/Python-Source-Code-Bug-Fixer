import numpy as np 

def function(x):

	n6 = 3
	t2 = 4
	paths = []
	try:
		if n6 >= 5:
			x = x+t2
			paths.append(1)
		else:
			n6 = x/n6
			paths.append(2)
		if t2 < 2:
			n6 = 4-n6
			x = 0*t2
			x = 9*x
			paths.append(3)
		else:
			x = x*7
			t2 = 9*t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))