import numpy as np 

def function(x):

	l0 = x
	a7 = x
	paths = []
	try:
		if x > 1:
			a7 = 8+a7
			paths.append(1)
		else:
			x = l0*x
			x = x-5
			paths.append(2)
		if l0 < 5:
			x = 4-x
			l0 = l0*2
			paths.append(3)
		else:
			x = a7+7
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))