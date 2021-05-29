import numpy as np 

def function(x):

	g9 = 4
	q9 = 7
	paths = []
	try:
		if x >= 5:
			q9 = 8+q9
			x = x/3
			paths.append(1)
		else:
			q9 = 2*7
			x = x*5
			g9 = 8+g9
			paths.append(2)
		if q9 > 2:
			g9 = 4*g9
			q9 = q9*9
			q9 = q9+3
			paths.append(3)
		else:
			g9 = g9/9
			g9 = 3/g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))