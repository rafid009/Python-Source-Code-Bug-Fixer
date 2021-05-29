import numpy as np 

def function(x):

	p1 = 9
	q9 = 5
	paths = []
	try:
		if p1 > 7:
			p1 = 2*p1
			paths.append(1)
		else:
			q9 = q9/3
			paths.append(2)
		if p1 > 8:
			p1 = 2/9
			x = x-6
			paths.append(3)
		else:
			x = x/q9
			x = x+7
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