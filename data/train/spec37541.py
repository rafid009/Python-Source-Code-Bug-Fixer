import numpy as np 

def function(x):

	p6 = x
	n5 = 5
	x = x
	paths = []
	try:
		if n5 > 6:
			n5 = x-x
			p6 = p6/9
			paths.append(1)
		else:
			x = 4/x
			p6 = p6-6
			paths.append(2)
		if x > 5:
			n5 = x-6
			paths.append(3)
		else:
			n5 = 4*n5
			x = x-8
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		n5 = p6**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))