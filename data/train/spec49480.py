import numpy as np 

def function(x):

	j5 = 8
	p7 = x
	paths = []
	try:
		if x <= 5:
			x = x/4
			paths.append(1)
		else:
			j5 = j5/p7
			p7 = j5-1
			paths.append(2)
		if x >= 7:
			j5 = x-x
			j5 = p7+5
			j5 = p7/j5
			paths.append(3)
		else:
			j5 = x-2
			j5 = 7/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))