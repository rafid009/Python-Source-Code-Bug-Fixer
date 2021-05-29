import numpy as np 

def function(x):

	f9 = x
	l5 = 6
	paths = []
	try:
		if x > 4:
			f9 = f9-3
			l5 = 0*4
			l5 = f9/8
			paths.append(1)
		else:
			l5 = 5+4
			l5 = l5*f9
			l5 = x-4
			paths.append(2)
		if x < 9:
			x = x+4
			paths.append(3)
		else:
			f9 = f9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))