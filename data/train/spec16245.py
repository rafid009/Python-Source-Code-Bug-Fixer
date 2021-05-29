import numpy as np 

def function(x):

	p6 = 8
	y8 = x
	paths = []
	try:
		if x <= 9:
			x = x/y8
			p6 = p6-5
			paths.append(1)
		else:
			x = y8/x
			p6 = x*p6
			p6 = p6/4
			paths.append(2)
		if p6 >= 8:
			p6 = 8-p6
			y8 = p6*7
			paths.append(3)
		else:
			p6 = 8-7
			p6 = 4+p6
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		p6 = y8**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))