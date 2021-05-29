import numpy as np 

def function(x):

	p1 = 8
	r2 = x
	paths = []
	try:
		if p1 <= 5:
			x = 5*5
			paths.append(1)
		else:
			r2 = r2*3
			p1 = p1/6
			p1 = 3/1
			paths.append(2)
		if r2 > 9:
			p1 = p1-4
			paths.append(3)
		else:
			p1 = 5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))