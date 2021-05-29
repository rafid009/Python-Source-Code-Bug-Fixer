import numpy as np 

def function(x):

	p8 = 2
	r1 = 1
	paths = []
	try:
		if x >= 9:
			x = 1*0
			x = x/2
			p8 = p8*5
			paths.append(1)
		else:
			p8 = p8*9
			x = p8*x
			paths.append(2)
		if p8 > 2:
			r1 = 7/p8
			r1 = 8-x
			r1 = r1*1
			paths.append(3)
		else:
			r1 = r1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))