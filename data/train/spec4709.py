import numpy as np 

def function(x):

	p6 = 2
	b6 = x
	paths = []
	try:
		if x <= 3:
			b6 = b6+6
			paths.append(1)
		else:
			x = 0-x
			x = 6+x
			paths.append(2)
		if p6 < 0:
			b6 = b6/5
			paths.append(3)
		else:
			b6 = b6+7
			b6 = b6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))