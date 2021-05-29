import numpy as np 

def function(x):

	p2 = x
	j1 = 2
	paths = []
	try:
		if j1 <= 7:
			j1 = 7/j1
			x = p2+j1
			paths.append(1)
		else:
			j1 = 9*j1
			paths.append(2)
		if j1 >= 8:
			x = x-6
			paths.append(3)
		else:
			x = x+3
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