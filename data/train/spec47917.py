import numpy as np 

def function(x):

	p1 = 9
	r3 = 9
	paths = []
	try:
		if r3 < 4:
			x = 4-8
			r3 = r3-1
			paths.append(1)
		else:
			r3 = r3*x
			r3 = r3/3
			paths.append(2)
		if r3 > 7:
			p1 = p1*5
			x = x+1
			paths.append(3)
		else:
			p1 = 3*p1
			x = x-p1
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