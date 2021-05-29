import numpy as np 

def function(x):

	l4 = x
	h7 = x
	paths = []
	try:
		if x > 6:
			x = 2*x
			x = x-5
			paths.append(1)
		else:
			x = x+7
			h7 = x-6
			x = x*9
			paths.append(2)
		if l4 <= 5:
			x = 4-x
			paths.append(3)
		else:
			h7 = h7*7
			h7 = h7+2
			l4 = x+6
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))