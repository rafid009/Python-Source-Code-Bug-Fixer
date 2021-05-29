import numpy as np 

def function(x):

	p4 = 1
	q0 = 8
	paths = []
	try:
		if q0 >= 2:
			q0 = q0/9
			x = x*7
			p4 = p4*3
			paths.append(1)
		else:
			q0 = q0*8
			q0 = q0*9
			paths.append(2)
		if q0 > 1:
			x = x*x
			q0 = 7/q0
			q0 = 2/8
			paths.append(3)
		else:
			q0 = x/q0
			p4 = p4-4
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