import numpy as np 

def function(x):

	l6 = 4
	e5 = x
	paths = []
	try:
		if e5 <= 8:
			e5 = e5/8
			e5 = e5+l6
			paths.append(1)
		else:
			l6 = 6-l6
			paths.append(2)
		if x > 3:
			e5 = e5+1
			x = l6/l6
			x = 1+x
			paths.append(3)
		else:
			x = 3*x
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		l6 = e5**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))