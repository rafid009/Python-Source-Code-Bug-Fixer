import numpy as np 

def function(x):

	a2 = x
	p1 = x
	paths = []
	try:
		if a2 >= 3:
			p1 = a2*p1
			a2 = 1/a2
			x = 7-x
			paths.append(1)
		else:
			p1 = 7/2
			p1 = p1-7
			paths.append(2)
		if a2 > 2:
			a2 = 2+a2
			paths.append(3)
		else:
			a2 = 6*4
			p1 = 7+7
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		a2 = p1**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))