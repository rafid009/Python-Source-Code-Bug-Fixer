import numpy as np 

def function(x):

	l9 = 8
	r4 = x
	paths = []
	try:
		if l9 <= 3:
			r4 = r4*r4
			l9 = r4/7
			paths.append(1)
		else:
			r4 = 0*r4
			x = 1/x
			paths.append(2)
		if l9 < 9:
			x = x/1
			paths.append(3)
		else:
			l9 = r4+l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))