import numpy as np 

def function(x):

	p4 = 5
	e9 = x
	paths = []
	try:
		if p4 >= 0:
			x = x+x
			paths.append(1)
		else:
			e9 = p4+7
			paths.append(2)
		if p4 <= 5:
			e9 = 9-e9
			paths.append(3)
		else:
			p4 = p4/3
			x = 2*1
			x = 8*e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))