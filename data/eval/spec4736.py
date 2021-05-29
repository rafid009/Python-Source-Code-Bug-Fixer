import numpy as np 

def function(x):

	h3 = 5
	l4 = x
	paths = []
	try:
		if x <= 4:
			x = 9+l4
			h3 = 4*x
			l4 = 3+x
			paths.append(1)
		else:
			h3 = h3-7
			paths.append(2)
		if x < 3:
			l4 = l4/5
			x = x/7
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		l4 = h3**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))