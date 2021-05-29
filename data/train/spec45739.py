import numpy as np 

def function(x):

	l8 = x
	r6 = 7
	paths = []
	try:
		if x >= 2:
			r6 = r6-6
			l8 = l8/4
			l8 = l8+8
			paths.append(1)
		else:
			x = 9+x
			r6 = r6/2
			r6 = r6+r6
			paths.append(2)
		if x <= 7:
			l8 = x+6
			l8 = l8-x
			x = 4-x
			paths.append(3)
		else:
			r6 = l8+6
			x = l8-8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))