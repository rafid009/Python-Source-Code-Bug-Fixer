import numpy as np 

def function(x):

	p1 = 9
	a1 = 5
	paths = []
	try:
		if p1 > 5:
			p1 = p1/5
			x = 7/x
			paths.append(1)
		else:
			p1 = p1+5
			x = p1*x
			p1 = p1*9
			paths.append(2)
		if x >= 0:
			p1 = p1-5
			a1 = a1*a1
			paths.append(3)
		else:
			x = 3-7
			p1 = 7+4
			p1 = p1*9
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