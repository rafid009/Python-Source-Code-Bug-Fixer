import numpy as np 

def function(x):

	h7 = 5
	l7 = x
	paths = []
	try:
		if l7 < 3:
			h7 = 6+h7
			l7 = l7-0
			h7 = h7/1
			paths.append(1)
		else:
			h7 = x-0
			l7 = l7*7
			x = x-8
			paths.append(2)
		if h7 <= 6:
			h7 = h7+6
			l7 = 5+5
			paths.append(3)
		else:
			x = l7+0
			x = x/4
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