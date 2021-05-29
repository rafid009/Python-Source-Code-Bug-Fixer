import numpy as np 

def function(x):

	i1 = 3
	v2 = x
	paths = []
	try:
		if i1 < 6:
			x = 9+x
			x = v2-3
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x >= 1:
			x = i1-x
			i1 = i1/7
			i1 = 5+8
			paths.append(3)
		else:
			i1 = x*i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		v2 = i1**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))