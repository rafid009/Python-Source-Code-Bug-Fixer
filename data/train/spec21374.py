import numpy as np 

def function(x):

	p4 = x
	q4 = 9
	paths = []
	try:
		if p4 <= 9:
			q4 = q4+q4
			q4 = q4*q4
			paths.append(1)
		else:
			x = x-0
			x = 5-x
			paths.append(2)
		if q4 >= 1:
			p4 = 2+7
			x = 4/x
			q4 = q4-q4
			paths.append(3)
		else:
			x = q4+p4
			p4 = p4*q4
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