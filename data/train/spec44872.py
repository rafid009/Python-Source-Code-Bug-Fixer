import numpy as np 

def function(x):

	p4 = x
	b4 = x
	paths = []
	try:
		if b4 > 8:
			x = b4-2
			paths.append(1)
		else:
			p4 = p4-8
			x = x+4
			b4 = x/1
			paths.append(2)
		if x > 4:
			p4 = 3/p4
			x = x-2
			paths.append(3)
		else:
			x = 3+x
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