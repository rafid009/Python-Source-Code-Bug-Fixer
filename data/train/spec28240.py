import numpy as np 

def function(x):

	e4 = 2
	l9 = 2
	paths = []
	try:
		if l9 >= 2:
			x = x-9
			l9 = l9-x
			paths.append(1)
		else:
			e4 = 2/2
			l9 = x+4
			paths.append(2)
		if e4 > 9:
			l9 = 8/9
			x = x/l9
			paths.append(3)
		else:
			e4 = 9+e4
			e4 = 2*5
			l9 = l9/3
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		e4 = l9**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))