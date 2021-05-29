import numpy as np 

def function(x):

	p6 = 1
	e2 = x
	paths = []
	try:
		if p6 <= 7:
			x = x*x
			p6 = 6/p6
			p6 = e2*p6
			paths.append(1)
		else:
			x = x-e2
			x = 2+x
			paths.append(2)
		if x >= 1:
			p6 = x*x
			e2 = 1+e2
			x = 0*7
			paths.append(3)
		else:
			e2 = e2*4
			e2 = 1/2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		p6 = e2**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))