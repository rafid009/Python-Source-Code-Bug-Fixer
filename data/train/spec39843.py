import numpy as np 

def function(x):

	e1 = 6
	p8 = x
	paths = []
	try:
		if p8 >= 3:
			p8 = p8+3
			paths.append(1)
		else:
			e1 = 7-7
			paths.append(2)
		if x >= 5:
			p8 = 8+e1
			x = 3-x
			paths.append(3)
		else:
			p8 = p8-4
			p8 = 1-0
			p8 = 5*x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))