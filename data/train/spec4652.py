import numpy as np 

def function(x):

	l5 = 6
	f0 = x
	paths = []
	try:
		if x < 4:
			x = 4*x
			paths.append(1)
		else:
			f0 = 4*f0
			l5 = l5/f0
			paths.append(2)
		if l5 > 1:
			l5 = 1+l5
			f0 = f0+7
			f0 = 4/f0
			paths.append(3)
		else:
			l5 = l5*f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))