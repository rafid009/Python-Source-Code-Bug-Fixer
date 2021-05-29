import numpy as np 

def function(x):

	q4 = 3
	p6 = x
	x = x
	paths = []
	try:
		if p6 < 4:
			x = x*3
			p6 = 0/q4
			p6 = 9-x
			paths.append(1)
		else:
			q4 = p6-q4
			paths.append(2)
		if x <= 7:
			q4 = q4/8
			p6 = 6+6
			p6 = 7*9
			paths.append(3)
		else:
			x = x/6
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