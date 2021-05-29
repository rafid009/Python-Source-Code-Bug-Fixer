import numpy as np 

def function(x):

	i1 = 0
	r5 = x
	paths = []
	try:
		if i1 <= 0:
			r5 = r5/4
			paths.append(1)
		else:
			x = x/x
			x = 7-8
			paths.append(2)
		if r5 >= 8:
			x = x-4
			x = 7+i1
			paths.append(3)
		else:
			r5 = 5/r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))