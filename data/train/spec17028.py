import numpy as np 

def function(x):

	q7 = x
	p6 = 2
	paths = []
	try:
		if x >= 2:
			x = 1-q7
			q7 = q7/1
			paths.append(1)
		else:
			q7 = x/3
			paths.append(2)
		if x > 7:
			p6 = p6*7
			paths.append(3)
		else:
			q7 = p6+q7
			q7 = q7/3
			p6 = p6*9
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))