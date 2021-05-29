import numpy as np 

def function(x):

	o1 = 3
	l3 = 5
	paths = []
	try:
		if x >= 1:
			l3 = l3-5
			l3 = l3*4
			paths.append(1)
		else:
			o1 = 4*o1
			x = x-0
			paths.append(2)
		if x < 7:
			l3 = 8*x
			paths.append(3)
		else:
			l3 = o1*x
			x = 3/x
			l3 = l3-4
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