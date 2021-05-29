import numpy as np 

def function(x):

	p6 = 2
	r3 = 6
	paths = []
	try:
		if p6 > 1:
			r3 = 3*r3
			p6 = p6/8
			paths.append(1)
		else:
			p6 = p6/x
			p6 = p6+6
			p6 = p6/1
			paths.append(2)
		if p6 >= 4:
			r3 = 7*8
			paths.append(3)
		else:
			x = x+p6
			p6 = p6/8
			p6 = 8/p6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))