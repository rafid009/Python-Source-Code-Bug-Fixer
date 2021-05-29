import numpy as np 

def function(x):

	i8 = x
	i6 = 9
	paths = []
	try:
		if i8 <= 1:
			i8 = 0-9
			paths.append(1)
		else:
			x = 2-i8
			paths.append(2)
		if i6 < 4:
			i8 = 6-i8
			x = 5-1
			i6 = i6*6
			paths.append(3)
		else:
			i8 = i8/i6
			i6 = 1*i6
			i6 = i6-i6
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))