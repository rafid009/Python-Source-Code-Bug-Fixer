import numpy as np 

def function(x):

	v5 = x
	l2 = 0
	paths = []
	try:
		if l2 >= 4:
			x = x*v5
			paths.append(1)
		else:
			x = 0-x
			v5 = v5-2
			paths.append(2)
		if l2 > 7:
			x = x*9
			l2 = 1*1
			v5 = v5-l2
			paths.append(3)
		else:
			l2 = l2*9
			x = 1*x
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