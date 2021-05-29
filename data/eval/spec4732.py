import numpy as np 

def function(x):

	l0 = 1
	d9 = x
	paths = []
	try:
		if d9 >= 5:
			l0 = l0*4
			l0 = l0*1
			d9 = 7+8
			paths.append(1)
		else:
			x = x*5
			x = x*9
			paths.append(2)
		if x < 3:
			d9 = d9+l0
			d9 = 4-1
			l0 = l0/9
			paths.append(3)
		else:
			x = d9/x
			d9 = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))