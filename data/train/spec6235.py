import numpy as np 

def function(x):

	p4 = 8
	q6 = 5
	paths = []
	try:
		if p4 < 3:
			q6 = p4-q6
			x = x+x
			paths.append(1)
		else:
			q6 = 4-q6
			p4 = p4/7
			paths.append(2)
		if q6 >= 5:
			x = 6/p4
			paths.append(3)
		else:
			p4 = p4/2
			q6 = q6+7
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))