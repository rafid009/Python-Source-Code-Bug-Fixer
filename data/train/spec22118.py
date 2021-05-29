import numpy as np 

def function(x):

	p2 = 1
	y7 = x
	paths = []
	try:
		if x < 0:
			x = x*8
			paths.append(1)
		else:
			p2 = p2+p2
			p2 = p2*0
			p2 = p2-2
			paths.append(2)
		if p2 < 5:
			p2 = x-6
			y7 = y7/2
			paths.append(3)
		else:
			y7 = 2*y7
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