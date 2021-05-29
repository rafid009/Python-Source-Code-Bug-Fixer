import numpy as np 

def function(x):

	l8 = 1
	v6 = x
	paths = []
	try:
		if l8 > 0:
			v6 = 4/l8
			v6 = v6/x
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if v6 > 0:
			v6 = 8*l8
			l8 = l8-6
			paths.append(3)
		else:
			l8 = l8/5
			l8 = v6-l8
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))