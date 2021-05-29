import numpy as np 

def function(x):

	q4 = 5
	p6 = x
	x = 4
	paths = []
	try:
		if p6 <= 6:
			q4 = x/q4
			q4 = q4*p6
			x = 3/7
			paths.append(1)
		else:
			x = 5*p6
			p6 = p6-7
			p6 = 5*x
			paths.append(2)
		if q4 <= 9:
			x = p6/x
			x = x-2
			paths.append(3)
		else:
			p6 = 5-p6
			p6 = 8+x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))