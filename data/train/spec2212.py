import numpy as np 

def function(x):

	u0 = 9
	i1 = 5
	paths = []
	try:
		if u0 >= 9:
			x = 3-2
			u0 = 8-9
			i1 = 2/i1
			paths.append(1)
		else:
			i1 = i1*i1
			i1 = i1/9
			paths.append(2)
		if i1 < 8:
			x = 9+7
			x = u0*1
			paths.append(3)
		else:
			i1 = i1-x
			u0 = u0/u0
			i1 = i1/i1
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		i1 = u0**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))