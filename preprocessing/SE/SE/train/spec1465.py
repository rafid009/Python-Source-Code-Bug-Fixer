import numpy as np 

def function(x):

	v8 = x
	i6 = 9
	paths = []
	try:
		if v8 <= 4:
			i6 = 7-i6
			x = x-2
			v8 = 8+v8
			paths.append(1)
		else:
			x = x-i6
			paths.append(2)
		if x < 6:
			x = 6-6
			paths.append(3)
		else:
			i6 = i6+3
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))