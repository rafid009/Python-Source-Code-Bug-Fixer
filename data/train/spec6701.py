import numpy as np 

def function(x):

	p3 = x
	h2 = x
	paths = []
	try:
		if h2 < 9:
			h2 = 0-h2
			paths.append(1)
		else:
			h2 = p3-6
			paths.append(2)
		if p3 <= 7:
			h2 = h2-x
			paths.append(3)
		else:
			h2 = h2-8
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))