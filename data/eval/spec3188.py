import numpy as np 

def function(x):

	b3 = 0
	p4 = 3
	x = x
	paths = []
	try:
		if b3 <= 7:
			b3 = x*3
			b3 = 4*b3
			paths.append(1)
		else:
			x = 6+p4
			x = 8-8
			p4 = p4+4
			paths.append(2)
		if b3 > 3:
			b3 = b3+9
			paths.append(3)
		else:
			p4 = 0/x
			p4 = p4+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))