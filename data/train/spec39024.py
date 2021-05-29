import numpy as np 

def function(x):

	b5 = 7
	g7 = x
	paths = []
	try:
		if x > 8:
			g7 = g7*2
			g7 = g7-g7
			g7 = g7*1
			paths.append(1)
		else:
			x = x/8
			g7 = x*g7
			b5 = b5/7
			paths.append(2)
		if x <= 4:
			g7 = 2-g7
			paths.append(3)
		else:
			g7 = g7*5
			g7 = g7-7
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))