import numpy as np 

def function(x):

	l7 = x
	e3 = 4
	paths = []
	try:
		if l7 >= 5:
			l7 = 5-l7
			e3 = 1/5
			paths.append(1)
		else:
			e3 = x*l7
			x = x-e3
			paths.append(2)
		if e3 >= 7:
			x = 2+x
			e3 = 7-e3
			paths.append(3)
		else:
			l7 = l7-2
			e3 = e3*5
			l7 = 3-l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))