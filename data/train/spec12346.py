import numpy as np 

def function(x):

	b1 = 1
	p2 = x
	paths = []
	try:
		if p2 > 5:
			x = 4*x
			x = 4-8
			p2 = 6*5
			paths.append(1)
		else:
			b1 = b1*9
			b1 = b1-3
			x = 3-7
			paths.append(2)
		if x > 0:
			x = x-1
			paths.append(3)
		else:
			p2 = p2+p2
			x = b1-5
			b1 = 9/b1
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))