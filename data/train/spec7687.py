import numpy as np 

def function(x):

	p1 = 9
	e8 = x
	x = 2
	paths = []
	try:
		if x >= 0:
			x = x/5
			paths.append(1)
		else:
			x = x-3
			p1 = p1-7
			p1 = p1-6
			paths.append(2)
		if e8 <= 2:
			p1 = p1/p1
			e8 = e8+e8
			paths.append(3)
		else:
			p1 = p1*p1
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		p1 = e8**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))