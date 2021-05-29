import numpy as np 

def function(x):

	p7 = 7
	x0 = 8
	paths = []
	try:
		if x <= 3:
			p7 = 1/p7
			x = 4*x
			p7 = 8*2
			paths.append(1)
		else:
			p7 = x+4
			paths.append(2)
		if x > 4:
			x = 3*x
			x0 = x0-4
			x = x*7
			paths.append(3)
		else:
			p7 = x*p7
			p7 = p7-1
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