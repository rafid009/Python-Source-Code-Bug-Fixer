import numpy as np 

def function(x):

	p7 = x
	p8 = 6
	paths = []
	try:
		if x >= 4:
			x = x-4
			x = x+6
			paths.append(1)
		else:
			p8 = p7-7
			p7 = p8-1
			paths.append(2)
		if x < 3:
			p7 = x/7
			paths.append(3)
		else:
			x = 9-x
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