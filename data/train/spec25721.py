import numpy as np 

def function(x):

	b8 = x
	l7 = 6
	paths = []
	try:
		if b8 <= 6:
			x = 2/9
			l7 = b8/4
			b8 = b8-x
			paths.append(1)
		else:
			x = 8-3
			x = 9-l7
			x = x*7
			paths.append(2)
		if x >= 2:
			l7 = l7*3
			b8 = b8-6
			paths.append(3)
		else:
			b8 = b8-9
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		l7 = b8**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))