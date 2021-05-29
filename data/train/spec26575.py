import numpy as np 

def function(x):

	a3 = x
	p1 = 8
	paths = []
	try:
		if p1 <= 5:
			x = x+7
			a3 = 6-8
			x = x+9
			paths.append(1)
		else:
			p1 = p1+a3
			paths.append(2)
		if a3 > 0:
			p1 = 2-p1
			a3 = a3-6
			paths.append(3)
		else:
			a3 = 7+a3
			a3 = a3-8
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