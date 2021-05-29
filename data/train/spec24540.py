import numpy as np 

def function(x):

	p4 = 3
	b7 = 0
	x = x
	paths = []
	try:
		if p4 <= 9:
			p4 = 8/9
			b7 = 0*5
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if p4 > 8:
			p4 = 7*p4
			paths.append(3)
		else:
			p4 = p4-x
			p4 = 1*p4
			b7 = b7-7
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