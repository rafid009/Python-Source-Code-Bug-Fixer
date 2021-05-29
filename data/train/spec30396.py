import numpy as np 

def function(x):

	l5 = x
	v1 = 0
	paths = []
	try:
		if x < 3:
			x = 4*x
			paths.append(1)
		else:
			x = x*5
			v1 = v1+8
			paths.append(2)
		if x >= 8:
			v1 = v1/3
			v1 = 2+v1
			paths.append(3)
		else:
			v1 = 0-9
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))