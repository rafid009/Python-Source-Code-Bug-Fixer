import numpy as np 

def function(x):

	q1 = x
	p6 = x
	paths = []
	try:
		if q1 <= 8:
			q1 = 3+x
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if p6 > 1:
			x = 8-x
			paths.append(3)
		else:
			p6 = 3/p6
			x = p6/7
			q1 = q1+6
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		p6 = q1**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))