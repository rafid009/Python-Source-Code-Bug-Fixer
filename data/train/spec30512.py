import numpy as np 

def function(x):

	v1 = x
	i4 = x
	x = x
	paths = []
	try:
		if v1 <= 1:
			x = v1/i4
			v1 = 0-v1
			paths.append(1)
		else:
			i4 = i4/1
			i4 = 5-i4
			paths.append(2)
		if x < 7:
			i4 = x-6
			v1 = 9/v1
			x = 8/3
			paths.append(3)
		else:
			v1 = v1/v1
			v1 = i4/3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))