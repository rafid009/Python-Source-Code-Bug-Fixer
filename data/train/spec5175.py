import numpy as np 

def function(x):

	r1 = x
	x6 = x
	paths = []
	try:
		if r1 > 0:
			r1 = r1+x
			paths.append(1)
		else:
			x6 = 4+x6
			x = r1/x
			paths.append(2)
		if r1 > 8:
			x = 3+x6
			x6 = r1-4
			r1 = r1*6
			paths.append(3)
		else:
			x = x/x6
			x = 8+5
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))