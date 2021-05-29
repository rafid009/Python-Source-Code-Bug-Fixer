import numpy as np 

def function(x):

	q3 = x
	l6 = x
	x = x
	paths = []
	try:
		if l6 <= 2:
			l6 = 4*l6
			l6 = 7-q3
			paths.append(1)
		else:
			l6 = l6/8
			l6 = q3*x
			paths.append(2)
		if l6 > 9:
			l6 = l6*l6
			x = x/4
			x = x+4
			paths.append(3)
		else:
			l6 = x*9
			q3 = 6+q3
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))