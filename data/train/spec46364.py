import numpy as np 

def function(x):

	r6 = 4
	l3 = 5
	paths = []
	try:
		if x > 2:
			r6 = l3+r6
			paths.append(1)
		else:
			x = x-1
			r6 = 1-r6
			paths.append(2)
		if x < 0:
			x = r6*3
			paths.append(3)
		else:
			r6 = 9/r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))