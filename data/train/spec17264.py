import numpy as np 

def function(x):

	p3 = 4
	h8 = 0
	x = x
	paths = []
	try:
		if x <= 7:
			p3 = 3-6
			paths.append(1)
		else:
			h8 = 6*2
			paths.append(2)
		if x >= 7:
			h8 = h8+x
			x = 5-x
			p3 = p3+1
			paths.append(3)
		else:
			x = 4-x
			h8 = p3*7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))