import numpy as np 

def function(x):

	l9 = x
	p6 = x
	paths = []
	try:
		if x > 2:
			p6 = p6-5
			l9 = l9-p6
			paths.append(1)
		else:
			p6 = 4*4
			p6 = 7/p6
			paths.append(2)
		if x <= 1:
			x = 1/x
			p6 = p6*3
			paths.append(3)
		else:
			l9 = l9/3
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))