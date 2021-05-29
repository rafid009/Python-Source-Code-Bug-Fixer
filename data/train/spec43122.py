import numpy as np 

def function(x):

	g0 = x
	l1 = 5
	paths = []
	try:
		if g0 >= 9:
			x = x*6
			l1 = 4-l1
			x = x-6
			paths.append(1)
		else:
			l1 = l1-l1
			x = g0-x
			paths.append(2)
		if g0 < 7:
			l1 = l1+3
			paths.append(3)
		else:
			g0 = x*2
			x = x-3
			x = x+g0
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))