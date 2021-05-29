import numpy as np 

def function(x):

	r6 = 3
	l7 = 7
	paths = []
	try:
		if x > 9:
			l7 = 0-x
			l7 = 4+l7
			r6 = 2/5
			paths.append(1)
		else:
			x = x+5
			r6 = 6*r6
			x = 5-x
			paths.append(2)
		if x >= 2:
			x = x*8
			l7 = 4-l7
			paths.append(3)
		else:
			r6 = r6*2
			r6 = r6/r6
			l7 = l7/l7
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