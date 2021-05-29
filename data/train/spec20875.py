import numpy as np 

def function(x):

	p7 = x
	p6 = x
	paths = []
	try:
		if p7 > 9:
			p6 = 7*7
			x = p7-x
			paths.append(1)
		else:
			x = x/6
			p6 = p6-5
			p7 = p7*8
			paths.append(2)
		if p7 > 9:
			x = 2-7
			x = x*p6
			paths.append(3)
		else:
			p6 = p6-5
			p7 = p7-8
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