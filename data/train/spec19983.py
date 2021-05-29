import numpy as np 

def function(x):

	f9 = 9
	l0 = x
	paths = []
	try:
		if x <= 0:
			f9 = 5-4
			l0 = l0/6
			paths.append(1)
		else:
			f9 = l0*l0
			l0 = l0-2
			paths.append(2)
		if f9 > 7:
			f9 = f9*6
			f9 = x+f9
			f9 = 7+l0
			paths.append(3)
		else:
			x = 8-x
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))