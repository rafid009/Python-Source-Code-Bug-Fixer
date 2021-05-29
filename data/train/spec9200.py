import numpy as np 

def function(x):

	h2 = x
	l9 = 5
	paths = []
	try:
		if x >= 0:
			l9 = x-l9
			x = 2+x
			h2 = 9*2
			paths.append(1)
		else:
			h2 = h2/6
			h2 = h2*5
			paths.append(2)
		if h2 <= 1:
			l9 = l9-h2
			h2 = h2+x
			paths.append(3)
		else:
			x = 9+x
			l9 = l9-9
			x = x/h2
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))