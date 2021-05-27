import numpy as np 

def function(x):

	n1 = x
	p6 = 7
	x = 5
	paths = []
	try:
		if x < 8:
			n1 = 3-2
			p6 = x-9
			x = x-1
			paths.append(1)
		else:
			p6 = p6+4
			paths.append(2)
		if p6 <= 0:
			x = 4*x
			n1 = n1/n1
			paths.append(3)
		else:
			p6 = 6*n1
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))