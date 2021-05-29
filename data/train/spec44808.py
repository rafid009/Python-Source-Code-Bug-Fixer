import numpy as np 

def function(x):

	j6 = x
	i1 = x
	paths = []
	try:
		if i1 <= 5:
			i1 = j6+i1
			paths.append(1)
		else:
			x = 7+8
			j6 = 8*7
			paths.append(2)
		if i1 <= 1:
			x = x-5
			paths.append(3)
		else:
			j6 = i1/j6
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