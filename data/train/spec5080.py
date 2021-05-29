import numpy as np 

def function(x):

	p1 = 1
	v5 = x
	paths = []
	try:
		if v5 >= 0:
			v5 = 4/v5
			v5 = p1-7
			p1 = p1-v5
			paths.append(1)
		else:
			p1 = v5*p1
			paths.append(2)
		if x < 5:
			p1 = x/p1
			x = x-9
			p1 = 9*v5
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))