import numpy as np 

def function(x):

	e6 = x
	n3 = 3
	x = x
	paths = []
	try:
		if x > 4:
			n3 = 3*n3
			x = x-n3
			paths.append(1)
		else:
			e6 = 1*e6
			e6 = e6-5
			x = 0/x
			paths.append(2)
		if n3 < 5:
			x = x+2
			paths.append(3)
		else:
			x = 4+x
			n3 = 7/n3
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))