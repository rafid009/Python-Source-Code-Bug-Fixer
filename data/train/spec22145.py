import numpy as np 

def function(x):

	p9 = x
	q1 = 8
	paths = []
	try:
		if q1 >= 7:
			p9 = 1/p9
			q1 = q1-q1
			paths.append(1)
		else:
			p9 = p9-x
			q1 = q1/9
			paths.append(2)
		if p9 >= 4:
			q1 = 2*q1
			p9 = 5-1
			q1 = 9*p9
			paths.append(3)
		else:
			x = p9+7
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))