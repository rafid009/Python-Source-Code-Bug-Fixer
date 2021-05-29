import numpy as np 

def function(x):

	p6 = 5
	n7 = 7
	paths = []
	try:
		if x >= 7:
			p6 = n7/3
			p6 = 1-p6
			x = x-p6
			paths.append(1)
		else:
			n7 = n7+6
			paths.append(2)
		if n7 >= 5:
			n7 = n7/4
			paths.append(3)
		else:
			p6 = 6*3
			x = n7-8
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))