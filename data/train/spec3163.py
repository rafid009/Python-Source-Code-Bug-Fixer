import numpy as np 

def function(x):

	p6 = 5
	b4 = x
	paths = []
	try:
		if x >= 8:
			b4 = b4-6
			p6 = b4-p6
			x = x-2
			paths.append(1)
		else:
			b4 = 3*x
			p6 = x-p6
			p6 = 4/p6
			paths.append(2)
		if b4 > 5:
			b4 = b4/1
			p6 = x-x
			p6 = x+4
			paths.append(3)
		else:
			b4 = 4-b4
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))