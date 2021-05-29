import numpy as np 

def function(x):

	l1 = 6
	h7 = x
	paths = []
	try:
		if h7 < 3:
			l1 = x*h7
			paths.append(1)
		else:
			x = x*l1
			paths.append(2)
		if l1 > 4:
			h7 = h7/l1
			paths.append(3)
		else:
			x = 6-l1
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		l1 = h7**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))