import numpy as np 

def function(x):

	l3 = 2
	e5 = 1
	paths = []
	try:
		if x < 9:
			l3 = 9-3
			e5 = 1/e5
			paths.append(1)
		else:
			l3 = 8/l3
			x = x*6
			paths.append(2)
		if e5 < 5:
			l3 = x*l3
			e5 = e5+x
			paths.append(3)
		else:
			e5 = e5-0
			l3 = l3-x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))