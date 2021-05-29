import numpy as np 

def function(x):

	r4 = x
	x3 = 5
	paths = []
	try:
		if x >= 6:
			r4 = 2-r4
			r4 = r4-r4
			paths.append(1)
		else:
			x3 = x+1
			x = x+4
			r4 = 4+x
			paths.append(2)
		if x <= 2:
			x3 = 6*x3
			x = x3*0
			x = 4*x
			paths.append(3)
		else:
			x3 = 8+x3
			x3 = r4-r4
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		r4 = x3**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))