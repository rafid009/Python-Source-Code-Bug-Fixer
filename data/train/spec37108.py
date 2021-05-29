import numpy as np 

def function(x):

	l4 = x
	e3 = 4
	paths = []
	try:
		if e3 < 5:
			l4 = l4+l4
			x = x*0
			paths.append(1)
		else:
			l4 = l4-9
			paths.append(2)
		if e3 > 4:
			e3 = 8/e3
			e3 = l4-9
			l4 = l4-9
			paths.append(3)
		else:
			e3 = 2/e3
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))