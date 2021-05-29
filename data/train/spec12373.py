import numpy as np 

def function(x):

	p3 = x
	y1 = x
	paths = []
	try:
		if p3 > 3:
			x = y1*x
			x = p3*2
			p3 = 8*p3
			paths.append(1)
		else:
			p3 = 3-y1
			paths.append(2)
		if p3 > 6:
			p3 = p3*8
			y1 = y1+p3
			paths.append(3)
		else:
			p3 = 9*p3
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))