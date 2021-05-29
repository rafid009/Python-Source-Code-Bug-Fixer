import numpy as np 

def function(x):

	r0 = x
	l6 = 2
	paths = []
	try:
		if x >= 9:
			x = x+x
			l6 = r0+0
			paths.append(1)
		else:
			x = x-9
			r0 = 6/3
			x = 4/x
			paths.append(2)
		if r0 <= 7:
			x = 5*x
			l6 = l6-1
			l6 = l6*3
			paths.append(3)
		else:
			x = 7-x
			x = x*x
			l6 = r0+l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))