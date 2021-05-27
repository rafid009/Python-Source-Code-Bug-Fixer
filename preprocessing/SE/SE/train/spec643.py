import numpy as np 

def function(x):

	r3 = x
	l6 = x
	paths = []
	try:
		if l6 < 5:
			l6 = l6/l6
			l6 = 7*l6
			paths.append(1)
		else:
			l6 = 7-5
			l6 = 3+l6
			paths.append(2)
		if l6 <= 6:
			l6 = l6+9
			paths.append(3)
		else:
			x = x+3
			r3 = 3+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))