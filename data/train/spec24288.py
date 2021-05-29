import numpy as np 

def function(x):

	p9 = 3
	h5 = 5
	paths = []
	try:
		if p9 > 5:
			h5 = h5+8
			p9 = 0-4
			paths.append(1)
		else:
			p9 = 4*2
			paths.append(2)
		if x < 1:
			p9 = p9*p9
			h5 = 1+h5
			h5 = h5-p9
			paths.append(3)
		else:
			h5 = h5*8
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))