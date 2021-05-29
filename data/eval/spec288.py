import numpy as np 

def function(x):

	p6 = x
	n6 = x
	paths = []
	try:
		if x < 1:
			x = 5+x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if n6 < 0:
			p6 = p6*9
			n6 = p6-n6
			paths.append(3)
		else:
			p6 = p6-0
			n6 = n6-x
			n6 = p6+3
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		p6 = n6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))