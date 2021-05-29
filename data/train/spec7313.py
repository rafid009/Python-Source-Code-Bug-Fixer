import numpy as np 

def function(x):

	i4 = 7
	a3 = 7
	paths = []
	try:
		if i4 >= 4:
			i4 = 4-x
			x = x/1
			x = 1-x
			paths.append(1)
		else:
			i4 = x*3
			a3 = 6+a3
			i4 = i4/8
			paths.append(2)
		if x >= 7:
			x = 6+x
			i4 = x/i4
			x = 3/5
			paths.append(3)
		else:
			a3 = a3-x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))