import numpy as np 

def function(x):

	p7 = 4
	e8 = x
	paths = []
	try:
		if e8 < 9:
			p7 = 8-6
			e8 = 6*e8
			e8 = 7+1
			paths.append(1)
		else:
			p7 = p7/3
			paths.append(2)
		if x < 9:
			e8 = e8-6
			e8 = x-e8
			p7 = p7/8
			paths.append(3)
		else:
			x = 9/x
			p7 = p7*e8
			x = 3+2
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))