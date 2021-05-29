import numpy as np 

def function(x):

	p3 = x
	q7 = x
	paths = []
	try:
		if p3 < 7:
			x = 4*x
			paths.append(1)
		else:
			p3 = 8/8
			paths.append(2)
		if x > 4:
			x = x-1
			paths.append(3)
		else:
			p3 = p3-9
			q7 = 7/q7
			q7 = q7+7
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