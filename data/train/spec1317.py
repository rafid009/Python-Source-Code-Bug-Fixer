import numpy as np 

def function(x):

	r6 = 8
	e4 = 2
	paths = []
	try:
		if x < 2:
			e4 = r6+2
			paths.append(1)
		else:
			r6 = r6*x
			r6 = 5+r6
			paths.append(2)
		if e4 > 7:
			r6 = r6/x
			e4 = 0+r6
			e4 = x-8
			paths.append(3)
		else:
			e4 = e4*9
			r6 = r6*6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))