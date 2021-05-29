import numpy as np 

def function(x):

	p4 = x
	b2 = x
	paths = []
	try:
		if x < 6:
			b2 = x+b2
			paths.append(1)
		else:
			x = 3*p4
			paths.append(2)
		if p4 <= 9:
			p4 = 8-1
			b2 = b2*2
			paths.append(3)
		else:
			p4 = p4*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))