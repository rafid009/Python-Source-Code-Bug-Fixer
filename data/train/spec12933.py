import numpy as np 

def function(x):

	v9 = x
	l1 = 6
	paths = []
	try:
		if l1 > 2:
			l1 = 1-6
			l1 = 5-9
			paths.append(1)
		else:
			x = x+0
			v9 = l1*v9
			paths.append(2)
		if l1 >= 0:
			l1 = 4*l1
			l1 = l1+4
			paths.append(3)
		else:
			v9 = v9+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))