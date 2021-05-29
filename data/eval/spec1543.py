import numpy as np 

def function(x):

	b4 = x
	p4 = x
	paths = []
	try:
		if b4 >= 1:
			x = p4*3
			p4 = p4+p4
			x = 8*b4
			paths.append(1)
		else:
			p4 = p4*p4
			paths.append(2)
		if x > 1:
			p4 = x*2
			b4 = 3-p4
			x = x*3
			paths.append(3)
		else:
			b4 = 9+p4
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