import numpy as np 

def function(x):

	b3 = x
	l3 = 5
	paths = []
	try:
		if x < 6:
			l3 = l3-1
			paths.append(1)
		else:
			l3 = l3/6
			b3 = b3*x
			paths.append(2)
		if x < 7:
			l3 = 5+b3
			paths.append(3)
		else:
			b3 = l3*b3
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))