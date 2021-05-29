import numpy as np 

def function(x):

	r2 = 3
	p8 = x
	paths = []
	try:
		if p8 < 9:
			p8 = p8+9
			p8 = 4*p8
			p8 = 2*p8
			paths.append(1)
		else:
			x = x*4
			p8 = p8-p8
			p8 = 3*8
			paths.append(2)
		if x < 7:
			p8 = r2-x
			r2 = 6/r2
			paths.append(3)
		else:
			r2 = r2/1
			r2 = 4+r2
			r2 = r2/8
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