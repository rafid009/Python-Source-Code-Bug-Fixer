import numpy as np 

def function(x):

	n4 = x
	p3 = 4
	paths = []
	try:
		if n4 > 7:
			n4 = n4+7
			n4 = p3-p3
			paths.append(1)
		else:
			n4 = n4+9
			paths.append(2)
		if n4 >= 1:
			p3 = 4*n4
			x = p3*x
			x = x/6
			paths.append(3)
		else:
			p3 = 1+p3
			p3 = p3*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))