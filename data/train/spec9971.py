import numpy as np 

def function(x):

	i1 = x
	n5 = 8
	paths = []
	try:
		if x > 4:
			x = x+7
			i1 = 2+n5
			paths.append(1)
		else:
			i1 = i1-4
			paths.append(2)
		if i1 > 7:
			n5 = 8*n5
			x = 4/5
			x = x-1
			paths.append(3)
		else:
			x = 2/x
			n5 = 9-5
			i1 = 7+i1
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