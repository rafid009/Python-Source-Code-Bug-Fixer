import numpy as np 

def function(x):

	t3 = x
	p1 = x
	paths = []
	try:
		if t3 < 5:
			x = x-7
			p1 = p1-9
			paths.append(1)
		else:
			p1 = p1+x
			paths.append(2)
		if t3 >= 8:
			x = x/1
			paths.append(3)
		else:
			x = x+p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))