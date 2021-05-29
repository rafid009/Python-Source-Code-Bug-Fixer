import numpy as np 

def function(x):

	q6 = 4
	p2 = 5
	x = 2
	paths = []
	try:
		if q6 > 9:
			x = x/p2
			paths.append(1)
		else:
			p2 = x-p2
			x = x/1
			paths.append(2)
		if q6 > 9:
			p2 = x+3
			paths.append(3)
		else:
			x = 4+x
			q6 = q6-6
			x = x*p2
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))