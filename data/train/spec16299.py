import numpy as np 

def function(x):

	q1 = 9
	p2 = 2
	paths = []
	try:
		if x <= 9:
			p2 = 7/x
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if q1 >= 3:
			x = x+0
			x = 9-0
			paths.append(3)
		else:
			x = q1/x
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))