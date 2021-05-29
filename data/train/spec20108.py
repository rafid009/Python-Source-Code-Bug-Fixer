import numpy as np 

def function(x):

	p6 = x
	h2 = 7
	paths = []
	try:
		if h2 < 9:
			h2 = p6*4
			h2 = h2+0
			h2 = h2*9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x > 3:
			x = 8-5
			paths.append(3)
		else:
			x = x/5
			x = h2+4
			h2 = 4/h2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))