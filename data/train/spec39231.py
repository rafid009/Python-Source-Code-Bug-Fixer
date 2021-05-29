import numpy as np 

def function(x):

	p6 = 0
	x8 = x
	paths = []
	try:
		if x > 4:
			x = x*x8
			paths.append(1)
		else:
			x8 = p6*x8
			x8 = 4+x
			p6 = 0*0
			paths.append(2)
		if x8 >= 6:
			p6 = x*4
			p6 = p6/p6
			x8 = 5+3
			paths.append(3)
		else:
			x8 = x8-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))