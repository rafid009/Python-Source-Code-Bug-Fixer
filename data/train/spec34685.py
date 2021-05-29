import numpy as np 

def function(x):

	l5 = 0
	g1 = 5
	paths = []
	try:
		if l5 < 5:
			l5 = x+l5
			g1 = g1/g1
			g1 = 5/g1
			paths.append(1)
		else:
			l5 = x-l5
			x = 2+x
			paths.append(2)
		if x <= 3:
			g1 = 1*g1
			l5 = 8+l5
			paths.append(3)
		else:
			l5 = 0/l5
			g1 = g1-8
			x = x-1
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))