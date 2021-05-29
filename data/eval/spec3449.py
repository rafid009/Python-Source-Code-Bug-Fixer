import numpy as np 

def function(x):

	h2 = 0
	l6 = x
	paths = []
	try:
		if x >= 7:
			x = l6+x
			x = x+5
			h2 = 7*h2
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if h2 <= 9:
			h2 = 5/4
			x = x+4
			l6 = 1*6
			paths.append(3)
		else:
			l6 = h2/3
			h2 = h2-6
			l6 = h2+l6
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