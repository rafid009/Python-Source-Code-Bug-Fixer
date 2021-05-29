import numpy as np 

def function(x):

	b4 = x
	l3 = x
	paths = []
	try:
		if x <= 2:
			b4 = 3/4
			paths.append(1)
		else:
			b4 = 1/b4
			paths.append(2)
		if x < 1:
			x = 1-l3
			b4 = b4+l3
			l3 = b4+l3
			paths.append(3)
		else:
			x = 4/l3
			x = x-b4
			x = x/2
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		l3 = b4**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))