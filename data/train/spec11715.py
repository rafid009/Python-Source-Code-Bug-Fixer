import numpy as np 

def function(x):

	i1 = 5
	v0 = x
	paths = []
	try:
		if i1 <= 6:
			i1 = v0+i1
			paths.append(1)
		else:
			v0 = v0/3
			x = 1/4
			i1 = v0/6
			paths.append(2)
		if i1 < 8:
			x = x+i1
			x = 7/8
			paths.append(3)
		else:
			v0 = v0-i1
			v0 = v0/7
			i1 = i1/i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))