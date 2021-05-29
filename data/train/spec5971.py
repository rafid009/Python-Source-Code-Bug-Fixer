import numpy as np 

def function(x):

	p8 = 1
	r9 = x
	paths = []
	try:
		if r9 <= 2:
			r9 = r9*5
			x = 3-x
			paths.append(1)
		else:
			r9 = r9-p8
			paths.append(2)
		if p8 < 3:
			x = x-1
			r9 = r9*1
			paths.append(3)
		else:
			r9 = r9+2
			r9 = r9+2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		p8 = r9**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))