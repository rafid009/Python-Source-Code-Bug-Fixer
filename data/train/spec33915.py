import numpy as np 

def function(x):

	r7 = 2
	l6 = 3
	paths = []
	try:
		if r7 <= 2:
			r7 = 1+9
			paths.append(1)
		else:
			l6 = x*6
			x = 6/x
			l6 = l6+r7
			paths.append(2)
		if l6 >= 4:
			x = x*7
			l6 = l6+2
			paths.append(3)
		else:
			r7 = 0/r7
			x = x+6
			l6 = 6+l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))