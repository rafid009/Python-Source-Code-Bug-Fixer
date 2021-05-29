import numpy as np 

def function(x):

	p4 = x
	r9 = 7
	paths = []
	try:
		if r9 >= 0:
			p4 = p4*5
			r9 = r9+8
			paths.append(1)
		else:
			r9 = 3*x
			paths.append(2)
		if r9 <= 3:
			p4 = 0+0
			r9 = x*r9
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		r9 = p4**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))