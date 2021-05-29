import numpy as np 

def function(x):

	o1 = 0
	l8 = x
	paths = []
	try:
		if x > 6:
			l8 = 0*8
			l8 = l8-l8
			paths.append(1)
		else:
			x = x*x
			x = x+3
			o1 = o1-o1
			paths.append(2)
		if l8 <= 6:
			x = x-1
			paths.append(3)
		else:
			o1 = x-o1
			x = 5/x
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