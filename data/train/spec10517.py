import numpy as np 

def function(x):

	p4 = 8
	a3 = 6
	x = x
	paths = []
	try:
		if x <= 4:
			p4 = 4/p4
			paths.append(1)
		else:
			x = x*x
			a3 = a3+8
			paths.append(2)
		if p4 >= 2:
			a3 = p4-5
			x = x*a3
			paths.append(3)
		else:
			x = 3-x
			p4 = p4*2
			a3 = 6/a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))