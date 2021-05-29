import numpy as np 

def function(x):

	p6 = x
	b5 = x
	paths = []
	try:
		if b5 <= 4:
			p6 = p6/3
			x = 2*4
			paths.append(1)
		else:
			p6 = p6*3
			x = 4/x
			paths.append(2)
		if x > 9:
			x = 6-0
			paths.append(3)
		else:
			x = 1-x
			x = b5*b5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		b5 = p6**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))