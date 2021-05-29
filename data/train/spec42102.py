import numpy as np 

def function(x):

	b0 = x
	p4 = 1
	paths = []
	try:
		if b0 <= 9:
			x = x-8
			b0 = 4+b0
			p4 = 6/b0
			paths.append(1)
		else:
			b0 = 4+4
			paths.append(2)
		if p4 >= 7:
			p4 = b0-p4
			p4 = p4-2
			p4 = p4+3
			paths.append(3)
		else:
			x = 0-p4
			p4 = 4/p4
			x = x-p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))