import numpy as np 

def function(x):

	j2 = x
	p2 = 3
	x = x
	paths = []
	try:
		if p2 < 5:
			j2 = j2*x
			paths.append(1)
		else:
			p2 = x-7
			paths.append(2)
		if p2 >= 2:
			x = x*j2
			x = 1+x
			paths.append(3)
		else:
			p2 = p2-2
			x = 5+3
			j2 = j2-0
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