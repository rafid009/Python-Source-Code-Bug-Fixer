import numpy as np 

def function(x):

	y1 = 3
	p3 = 6
	paths = []
	try:
		if x >= 7:
			y1 = x*2
			x = x*1
			paths.append(1)
		else:
			p3 = p3-y1
			paths.append(2)
		if p3 >= 2:
			y1 = y1+x
			p3 = y1/y1
			p3 = 8/8
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))