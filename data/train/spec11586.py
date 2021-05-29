import numpy as np 

def function(x):

	l2 = x
	e4 = x
	paths = []
	try:
		if e4 <= 2:
			e4 = e4+1
			l2 = l2-e4
			x = x+0
			paths.append(1)
		else:
			l2 = l2/3
			e4 = 6-e4
			l2 = l2*8
			paths.append(2)
		if x < 4:
			e4 = e4+e4
			e4 = e4*x
			l2 = 8*1
			paths.append(3)
		else:
			e4 = 6+e4
			l2 = l2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))