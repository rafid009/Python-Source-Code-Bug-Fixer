import numpy as np 

def function(x):

	p8 = x
	d9 = x
	paths = []
	try:
		if p8 >= 5:
			d9 = 2*x
			d9 = d9*7
			p8 = p8-p8
			paths.append(1)
		else:
			p8 = 0+5
			paths.append(2)
		if x < 1:
			x = x/x
			paths.append(3)
		else:
			p8 = 7+8
			x = p8-x
			d9 = 3*d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		p8 = d9**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))