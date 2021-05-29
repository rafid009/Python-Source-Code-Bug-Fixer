import numpy as np 

def function(x):

	e2 = 3
	p7 = 3
	paths = []
	try:
		if p7 >= 9:
			x = x+x
			p7 = x/6
			p7 = 1-7
			paths.append(1)
		else:
			p7 = p7*1
			paths.append(2)
		if x > 4:
			e2 = e2*x
			x = p7/5
			e2 = e2-7
			paths.append(3)
		else:
			x = x-1
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