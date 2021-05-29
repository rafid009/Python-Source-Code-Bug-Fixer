import numpy as np 

def function(x):

	u3 = 2
	g8 = 6
	paths = []
	try:
		if g8 >= 5:
			u3 = x-u3
			paths.append(1)
		else:
			x = x/1
			g8 = 4/g8
			paths.append(2)
		if x > 2:
			g8 = g8/6
			g8 = x*7
			paths.append(3)
		else:
			u3 = 8+x
			g8 = 9*g8
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))