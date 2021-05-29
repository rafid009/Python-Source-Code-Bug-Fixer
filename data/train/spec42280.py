import numpy as np 

def function(x):

	p3 = 5
	p6 = 7
	paths = []
	try:
		if x >= 2:
			p6 = p6-9
			paths.append(1)
		else:
			p6 = p6-3
			p3 = x-3
			paths.append(2)
		if x <= 8:
			x = 1+1
			paths.append(3)
		else:
			p3 = 9-0
			x = 4-5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p3 = p6**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))