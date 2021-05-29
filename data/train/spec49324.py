import numpy as np 

def function(x):

	l6 = 7
	e6 = 6
	paths = []
	try:
		if l6 <= 7:
			x = x-x
			paths.append(1)
		else:
			l6 = l6-l6
			paths.append(2)
		if l6 <= 5:
			e6 = e6-7
			x = x*7
			x = 0-1
			paths.append(3)
		else:
			e6 = x-l6
			l6 = 9/e6
			l6 = 2-l6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		l6 = e6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))