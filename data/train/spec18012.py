import numpy as np 

def function(x):

	p6 = 8
	i1 = 5
	paths = []
	try:
		if p6 < 2:
			x = 5/x
			x = 2/x
			p6 = x/i1
			paths.append(1)
		else:
			i1 = i1*x
			i1 = x/p6
			paths.append(2)
		if x > 6:
			i1 = 1/i1
			paths.append(3)
		else:
			p6 = p6/6
			p6 = i1/p6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))