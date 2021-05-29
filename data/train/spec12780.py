import numpy as np 

def function(x):

	e8 = x
	n3 = x
	paths = []
	try:
		if x >= 5:
			n3 = 7-n3
			x = 6+4
			x = x-1
			paths.append(1)
		else:
			x = x-0
			x = x-1
			e8 = e8*x
			paths.append(2)
		if x > 4:
			n3 = n3*2
			n3 = 8*n3
			paths.append(3)
		else:
			e8 = n3/e8
			e8 = x*e8
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))