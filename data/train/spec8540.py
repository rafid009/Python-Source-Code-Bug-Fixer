import numpy as np 

def function(x):

	p4 = x
	j1 = 2
	paths = []
	try:
		if x < 4:
			p4 = p4+4
			p4 = p4*7
			paths.append(1)
		else:
			p4 = 1/9
			paths.append(2)
		if p4 > 1:
			p4 = 6*x
			j1 = 9+j1
			x = x+6
			paths.append(3)
		else:
			p4 = p4*3
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))