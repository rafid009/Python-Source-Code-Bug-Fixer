import numpy as np 

def function(x):

	j6 = 6
	v8 = x
	x = 7
	paths = []
	try:
		if j6 > 9:
			v8 = 4/v8
			j6 = 0-v8
			j6 = 3-8
			paths.append(1)
		else:
			x = 9-7
			paths.append(2)
		if x < 6:
			v8 = v8-7
			paths.append(3)
		else:
			x = 9/4
			j6 = 9+j6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))