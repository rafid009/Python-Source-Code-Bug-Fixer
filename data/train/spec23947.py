import numpy as np 

def function(x):

	g9 = 1
	j7 = 6
	paths = []
	try:
		if x < 0:
			g9 = g9/j7
			g9 = g9+1
			x = x-6
			paths.append(1)
		else:
			g9 = x+9
			x = j7-j7
			paths.append(2)
		if g9 >= 7:
			x = x/5
			x = x+4
			paths.append(3)
		else:
			x = x*5
			j7 = 5/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))