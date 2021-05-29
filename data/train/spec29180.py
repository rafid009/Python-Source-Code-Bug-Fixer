import numpy as np 

def function(x):

	l6 = x
	r1 = 4
	x = x
	paths = []
	try:
		if l6 <= 7:
			r1 = r1*r1
			x = x/6
			paths.append(1)
		else:
			l6 = l6-4
			x = x-8
			paths.append(2)
		if x <= 7:
			l6 = l6/8
			r1 = l6-3
			paths.append(3)
		else:
			l6 = 8-l6
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