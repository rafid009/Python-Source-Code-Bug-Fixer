import numpy as np 

def function(x):

	l4 = x
	e4 = x
	paths = []
	try:
		if l4 > 9:
			x = 2-9
			paths.append(1)
		else:
			l4 = x*6
			paths.append(2)
		if e4 < 7:
			x = l4/l4
			x = e4*x
			paths.append(3)
		else:
			x = x/8
			l4 = 7-2
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		l4 = e4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))