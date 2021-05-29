import numpy as np 

def function(x):

	p2 = 4
	v1 = 7
	paths = []
	try:
		if v1 >= 1:
			p2 = x+0
			x = 6-7
			x = x*5
			paths.append(1)
		else:
			p2 = 4/v1
			paths.append(2)
		if x < 5:
			p2 = p2-6
			v1 = v1/p2
			paths.append(3)
		else:
			v1 = 2*p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))