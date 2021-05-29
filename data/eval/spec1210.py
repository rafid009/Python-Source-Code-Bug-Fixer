import numpy as np 

def function(x):

	k5 = 0
	p3 = 1
	paths = []
	try:
		if k5 >= 3:
			x = p3*8
			paths.append(1)
		else:
			p3 = 2+p3
			x = x-7
			p3 = 7/4
			paths.append(2)
		if x >= 8:
			x = p3*8
			x = x/2
			paths.append(3)
		else:
			p3 = x/7
			x = x*8
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