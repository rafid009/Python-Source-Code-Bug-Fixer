import numpy as np 

def function(x):

	p6 = x
	p7 = x
	paths = []
	try:
		if x <= 7:
			x = x*9
			paths.append(1)
		else:
			x = 1/3
			p7 = p7*1
			x = x+8
			paths.append(2)
		if p6 <= 8:
			p7 = 6*p7
			p6 = 2/p6
			paths.append(3)
		else:
			p6 = 0+p7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))