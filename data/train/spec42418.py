import numpy as np 

def function(x):

	l9 = x
	e3 = x
	paths = []
	try:
		if x >= 1:
			e3 = e3-9
			x = x*x
			paths.append(1)
		else:
			l9 = 6/l9
			e3 = e3/1
			x = 7/l9
			paths.append(2)
		if x > 8:
			l9 = e3/l9
			e3 = 4-e3
			e3 = 5*e3
			paths.append(3)
		else:
			e3 = 6+8
			e3 = e3+7
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		e3 = l9**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))