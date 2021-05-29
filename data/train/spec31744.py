import numpy as np 

def function(x):

	p2 = 1
	j5 = x
	paths = []
	try:
		if x >= 3:
			j5 = j5-5
			x = 1+2
			p2 = 2-4
			paths.append(1)
		else:
			j5 = 5/j5
			j5 = 5/3
			p2 = 1+p2
			paths.append(2)
		if x <= 9:
			p2 = j5*j5
			p2 = 6*p2
			paths.append(3)
		else:
			j5 = 3/j5
			j5 = 8/p2
			x = 8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))