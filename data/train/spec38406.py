import numpy as np 

def function(x):

	b2 = x
	p1 = x
	paths = []
	try:
		if x >= 1:
			b2 = b2-b2
			x = b2+x
			p1 = x-b2
			paths.append(1)
		else:
			b2 = b2/1
			b2 = b2+8
			b2 = b2+6
			paths.append(2)
		if p1 <= 0:
			p1 = 4/p1
			p1 = p1-2
			paths.append(3)
		else:
			p1 = x*1
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		p1 = b2**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))