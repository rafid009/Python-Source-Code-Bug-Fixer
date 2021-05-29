import numpy as np 

def function(x):

	l4 = x
	e1 = x
	paths = []
	try:
		if l4 < 2:
			e1 = e1/6
			paths.append(1)
		else:
			x = e1-8
			e1 = e1-3
			paths.append(2)
		if x > 3:
			l4 = l4+2
			paths.append(3)
		else:
			l4 = 8*6
			e1 = 8/e1
			x = 3/4
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		l4 = e1**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))