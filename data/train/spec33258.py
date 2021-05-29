import numpy as np 

def function(x):

	w8 = 7
	l5 = 0
	x = 6
	paths = []
	try:
		if l5 <= 0:
			w8 = 1-w8
			x = x*9
			x = 3*x
			paths.append(1)
		else:
			w8 = w8/2
			paths.append(2)
		if l5 < 1:
			x = 3+w8
			w8 = w8*6
			paths.append(3)
		else:
			x = 6-5
			l5 = 7+l5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))