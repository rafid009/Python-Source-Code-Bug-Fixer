import numpy as np 

def function(x):

	b9 = 4
	p3 = 2
	paths = []
	try:
		if x > 0:
			x = x-8
			x = 1-5
			p3 = 7-2
			paths.append(1)
		else:
			b9 = b9-4
			b9 = b9*5
			b9 = b9-b9
			paths.append(2)
		if b9 >= 7:
			p3 = b9*p3
			b9 = b9/5
			b9 = 5/b9
			paths.append(3)
		else:
			p3 = p3-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))