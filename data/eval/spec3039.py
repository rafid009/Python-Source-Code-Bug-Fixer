import numpy as np 

def function(x):

	q4 = 2
	p2 = x
	paths = []
	try:
		if p2 <= 3:
			p2 = p2*9
			q4 = q4*2
			paths.append(1)
		else:
			q4 = 6/q4
			paths.append(2)
		if q4 <= 6:
			x = 1/x
			paths.append(3)
		else:
			x = 3+0
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		q4 = p2**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))