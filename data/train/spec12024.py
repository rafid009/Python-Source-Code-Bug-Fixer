import numpy as np 

def function(x):

	x6 = 0
	r7 = x
	x = x
	paths = []
	try:
		if x6 < 2:
			x = 3-8
			paths.append(1)
		else:
			x = 6*6
			r7 = r7*x6
			paths.append(2)
		if x6 > 9:
			x = x+1
			paths.append(3)
		else:
			x6 = x6+r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))