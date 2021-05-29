import numpy as np 

def function(x):

	p8 = x
	r4 = x
	paths = []
	try:
		if x >= 9:
			x = 4/x
			paths.append(1)
		else:
			x = 1+x
			x = x+7
			r4 = r4-0
			paths.append(2)
		if r4 >= 9:
			p8 = p8+2
			p8 = r4*7
			paths.append(3)
		else:
			x = r4/x
			r4 = p8-p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		r4 = p8**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))