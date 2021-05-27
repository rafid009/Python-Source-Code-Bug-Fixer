import numpy as np 

def function(x):

	f3 = 8
	l0 = x
	paths = []
	try:
		if f3 < 0:
			l0 = l0*4
			paths.append(1)
		else:
			f3 = f3*9
			l0 = l0*7
			f3 = l0/f3
			paths.append(2)
		if l0 < 1:
			f3 = x+f3
			l0 = l0-l0
			f3 = 6-f3
			paths.append(3)
		else:
			f3 = 9+f3
			x = 6+4
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