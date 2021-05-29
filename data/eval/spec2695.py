import numpy as np 

def function(x):

	q0 = 8
	l8 = 3
	paths = []
	try:
		if x > 4:
			x = q0/1
			l8 = l8*1
			x = x/x
			paths.append(1)
		else:
			l8 = x*2
			q0 = q0+1
			l8 = l8-x
			paths.append(2)
		if q0 > 6:
			l8 = l8+8
			paths.append(3)
		else:
			x = x/1
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