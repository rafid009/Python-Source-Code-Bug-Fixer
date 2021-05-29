import numpy as np 

def function(x):

	d9 = x
	i4 = 5
	paths = []
	try:
		if x > 5:
			x = i4*6
			i4 = d9-i4
			i4 = i4*x
			paths.append(1)
		else:
			x = 4*2
			paths.append(2)
		if i4 > 4:
			d9 = 6-d9
			i4 = 8+6
			paths.append(3)
		else:
			x = x/1
			x = i4-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))