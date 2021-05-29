import numpy as np 

def function(x):

	n4 = 2
	e1 = 2
	paths = []
	try:
		if n4 < 0:
			n4 = 0+n4
			n4 = 2/7
			paths.append(1)
		else:
			x = x*6
			x = 6*x
			n4 = 2/8
			paths.append(2)
		if x > 4:
			e1 = 0+x
			n4 = x-9
			x = x-e1
			paths.append(3)
		else:
			n4 = 3*e1
			e1 = x+4
			e1 = e1-5
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		n4 = e1**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))