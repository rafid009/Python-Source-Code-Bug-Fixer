import numpy as np 

def function(x):

	l8 = 6
	l0 = 1
	paths = []
	try:
		if l8 < 3:
			l0 = 0*6
			paths.append(1)
		else:
			l8 = l8*0
			x = 8/x
			l0 = l0-9
			paths.append(2)
		if l8 < 7:
			l0 = l0+x
			l0 = l0-4
			x = 0+x
			paths.append(3)
		else:
			l0 = l0/8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l8 = l0**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))