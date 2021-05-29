import numpy as np 

def function(x):

	b4 = 2
	p4 = 9
	paths = []
	try:
		if x < 1:
			x = p4/x
			x = p4/x
			paths.append(1)
		else:
			x = 3+x
			b4 = b4-b4
			paths.append(2)
		if x < 2:
			p4 = p4*9
			x = x*4
			x = 6/x
			paths.append(3)
		else:
			x = p4-0
			x = b4/x
			p4 = p4+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))