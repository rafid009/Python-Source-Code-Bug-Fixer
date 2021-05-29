import numpy as np 

def function(x):

	p7 = x
	p8 = x
	paths = []
	try:
		if p8 < 5:
			x = p7*x
			x = x-0
			x = 6*x
			paths.append(1)
		else:
			x = x-0
			p8 = p8+2
			paths.append(2)
		if p7 >= 2:
			x = x*6
			p7 = 1/p7
			paths.append(3)
		else:
			x = p8-p8
			p7 = 1*7
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