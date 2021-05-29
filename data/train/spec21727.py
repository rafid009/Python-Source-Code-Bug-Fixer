import numpy as np 

def function(x):

	r2 = 2
	p7 = 5
	paths = []
	try:
		if x <= 6:
			x = r2/8
			p7 = p7+7
			p7 = 9-p7
			paths.append(1)
		else:
			p7 = p7/p7
			p7 = p7+8
			paths.append(2)
		if x < 8:
			p7 = 6-p7
			r2 = 3/r2
			r2 = r2-r2
			paths.append(3)
		else:
			r2 = r2/x
			p7 = 8-p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))