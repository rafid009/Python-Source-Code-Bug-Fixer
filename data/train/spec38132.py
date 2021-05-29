import numpy as np 

def function(x):

	p6 = x
	p7 = 2
	paths = []
	try:
		if p6 >= 0:
			p6 = p7+4
			x = 4-x
			paths.append(1)
		else:
			x = x+8
			x = p7*p7
			p7 = p6*p6
			paths.append(2)
		if x >= 2:
			p7 = p7*6
			paths.append(3)
		else:
			p7 = 3*1
			p6 = 0-0
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p7 = p6**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))