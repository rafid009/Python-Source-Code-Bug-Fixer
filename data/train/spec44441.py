import numpy as np 

def function(x):

	i1 = x
	r3 = 1
	paths = []
	try:
		if x > 5:
			x = r3*6
			i1 = 9+i1
			paths.append(1)
		else:
			i1 = r3*i1
			i1 = i1/6
			paths.append(2)
		if r3 < 5:
			r3 = 9*r3
			r3 = r3+0
			i1 = i1/4
			paths.append(3)
		else:
			r3 = 4/r3
			x = 8-1
			i1 = x/i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))