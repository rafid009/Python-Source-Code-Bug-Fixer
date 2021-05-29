import numpy as np 

def function(x):

	n5 = 7
	p3 = x
	paths = []
	try:
		if n5 > 0:
			x = x-6
			n5 = n5+3
			paths.append(1)
		else:
			p3 = p3-p3
			paths.append(2)
		if x >= 7:
			n5 = 0+4
			paths.append(3)
		else:
			n5 = 8-0
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))