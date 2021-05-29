import numpy as np 

def function(x):

	q7 = x
	p1 = 3
	paths = []
	try:
		if x > 3:
			q7 = q7+x
			x = 8/9
			paths.append(1)
		else:
			q7 = 2*q7
			q7 = 9+p1
			paths.append(2)
		if q7 <= 8:
			q7 = 4+2
			x = p1-x
			p1 = p1-8
			paths.append(3)
		else:
			p1 = p1-p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))