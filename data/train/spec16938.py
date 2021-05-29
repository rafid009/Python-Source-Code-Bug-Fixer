import numpy as np 

def function(x):

	l3 = x
	f2 = 7
	paths = []
	try:
		if l3 > 3:
			l3 = l3+6
			x = 0/x
			paths.append(1)
		else:
			x = 8-x
			f2 = f2+7
			x = l3*x
			paths.append(2)
		if l3 > 6:
			f2 = f2-3
			f2 = f2*x
			paths.append(3)
		else:
			x = 0-f2
			f2 = 4/f2
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