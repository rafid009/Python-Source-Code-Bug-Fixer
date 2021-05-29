import numpy as np 

def function(x):

	l3 = x
	l8 = 3
	paths = []
	try:
		if l3 >= 5:
			l3 = l3*2
			l8 = 5-7
			x = x/3
			paths.append(1)
		else:
			l8 = l8-6
			l3 = 4+3
			paths.append(2)
		if l8 >= 9:
			x = x-l8
			l8 = l8-l8
			l3 = 1/l3
			paths.append(3)
		else:
			x = x-0
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