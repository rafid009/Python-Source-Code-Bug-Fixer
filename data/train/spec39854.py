import numpy as np 

def function(x):

	n4 = 2
	p6 = x
	paths = []
	try:
		if p6 <= 1:
			p6 = x*8
			p6 = p6+0
			x = 0/6
			paths.append(1)
		else:
			p6 = 3/p6
			x = 6+6
			x = x/4
			paths.append(2)
		if p6 < 6:
			x = x*5
			x = 9-x
			paths.append(3)
		else:
			n4 = p6+n4
			x = 8-6
			p6 = p6*6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		n4 = p6**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))