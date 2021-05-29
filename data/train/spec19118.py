import numpy as np 

def function(x):

	p7 = 2
	m2 = x
	paths = []
	try:
		if x >= 1:
			p7 = m2/2
			m2 = 1-0
			paths.append(1)
		else:
			x = x-6
			m2 = x-2
			p7 = 3-x
			paths.append(2)
		if m2 < 0:
			x = 1/x
			x = 9*7
			x = 1-x
			paths.append(3)
		else:
			p7 = 7*p7
			p7 = 3-p7
			p7 = p7/p7
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