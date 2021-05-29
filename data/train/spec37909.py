import numpy as np 

def function(x):

	r4 = 3
	l6 = x
	paths = []
	try:
		if l6 < 7:
			l6 = 4+6
			x = x+8
			x = 4-x
			paths.append(1)
		else:
			x = x+3
			x = x/l6
			r4 = 3-l6
			paths.append(2)
		if l6 < 4:
			r4 = x-8
			x = x+4
			paths.append(3)
		else:
			l6 = x/l6
			l6 = l6*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))