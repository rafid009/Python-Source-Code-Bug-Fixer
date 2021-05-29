import numpy as np 

def function(x):

	a8 = 4
	p6 = 7
	paths = []
	try:
		if x >= 5:
			p6 = 6*a8
			paths.append(1)
		else:
			p6 = p6-6
			paths.append(2)
		if p6 < 2:
			a8 = a8*4
			a8 = a8-8
			a8 = 4*x
			paths.append(3)
		else:
			x = x+x
			x = 0/x
			a8 = a8+1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))