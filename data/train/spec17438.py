import numpy as np 

def function(x):

	q3 = x
	p7 = 2
	paths = []
	try:
		if p7 >= 8:
			p7 = q3*4
			q3 = 2/q3
			paths.append(1)
		else:
			x = q3+7
			paths.append(2)
		if p7 >= 7:
			q3 = q3/q3
			p7 = p7-4
			q3 = x/3
			paths.append(3)
		else:
			q3 = 2-q3
			p7 = 6+2
			q3 = 2/q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))