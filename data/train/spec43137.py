import numpy as np 

def function(x):

	v2 = x
	i4 = 5
	paths = []
	try:
		if x < 4:
			x = x-x
			i4 = v2*v2
			i4 = 4-i4
			paths.append(1)
		else:
			i4 = i4+v2
			x = 7/9
			paths.append(2)
		if x > 8:
			i4 = 6-i4
			paths.append(3)
		else:
			v2 = 3/i4
			i4 = i4+5
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		v2 = i4**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))