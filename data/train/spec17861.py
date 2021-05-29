import numpy as np 

def function(x):

	l6 = x
	f6 = 9
	paths = []
	try:
		if x < 5:
			l6 = x*5
			f6 = 7-f6
			f6 = l6/f6
			paths.append(1)
		else:
			l6 = 8*l6
			x = x/8
			l6 = 5/7
			paths.append(2)
		if f6 < 2:
			l6 = l6-3
			l6 = l6+2
			paths.append(3)
		else:
			f6 = f6*f6
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