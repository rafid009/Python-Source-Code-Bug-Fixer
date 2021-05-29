import numpy as np 

def function(x):

	k1 = x
	l8 = 9
	paths = []
	try:
		if k1 <= 8:
			k1 = 0+k1
			k1 = 8+l8
			k1 = 2*l8
			paths.append(1)
		else:
			l8 = l8*x
			x = x+l8
			paths.append(2)
		if k1 >= 9:
			l8 = l8/3
			l8 = x/5
			x = x+4
			paths.append(3)
		else:
			l8 = l8/l8
			x = 7+x
			l8 = l8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))