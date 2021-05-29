import numpy as np 

def function(x):

	l3 = x
	v7 = 2
	paths = []
	try:
		if x > 9:
			l3 = l3*6
			paths.append(1)
		else:
			l3 = l3+l3
			paths.append(2)
		if x >= 2:
			v7 = x/l3
			paths.append(3)
		else:
			v7 = 2+9
			l3 = 7/l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))