import numpy as np 

def function(x):

	p0 = x
	p8 = x
	paths = []
	try:
		if x >= 9:
			x = x+7
			paths.append(1)
		else:
			p0 = 7-p0
			x = x-3
			paths.append(2)
		if p8 > 6:
			p0 = 0+3
			paths.append(3)
		else:
			x = p0*5
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