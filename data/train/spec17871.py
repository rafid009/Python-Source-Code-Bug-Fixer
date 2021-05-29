import numpy as np 

def function(x):

	r1 = x
	i1 = 8
	paths = []
	try:
		if x > 6:
			i1 = 0*0
			paths.append(1)
		else:
			i1 = 0*i1
			paths.append(2)
		if x >= 6:
			r1 = r1-1
			i1 = i1/3
			paths.append(3)
		else:
			i1 = 1-r1
			i1 = 9*r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))