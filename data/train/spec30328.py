import numpy as np 

def function(x):

	v6 = 5
	i4 = x
	paths = []
	try:
		if x >= 9:
			i4 = i4*x
			paths.append(1)
		else:
			v6 = v6+8
			v6 = 8+v6
			i4 = i4+5
			paths.append(2)
		if i4 >= 7:
			x = x-7
			v6 = 4/v6
			paths.append(3)
		else:
			x = 7+x
			x = 7-v6
			v6 = v6+6
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