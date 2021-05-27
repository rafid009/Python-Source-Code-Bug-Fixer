import numpy as np 

def function(x):

	q6 = 6
	p9 = x
	paths = []
	try:
		if q6 >= 8:
			q6 = 1-p9
			paths.append(1)
		else:
			p9 = x-0
			q6 = 5-4
			x = x/2
			paths.append(2)
		if x >= 1:
			p9 = p9+4
			paths.append(3)
		else:
			q6 = 2*q6
			q6 = q6*6
			x = 2*3
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