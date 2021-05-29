import numpy as np 

def function(x):

	i8 = x
	o3 = x
	paths = []
	try:
		if o3 >= 5:
			x = i8/1
			i8 = i8-i8
			x = x-3
			paths.append(1)
		else:
			o3 = 4*o3
			o3 = x*i8
			i8 = i8*8
			paths.append(2)
		if x > 6:
			o3 = 9+9
			x = 9-5
			i8 = 8/7
			paths.append(3)
		else:
			o3 = i8+o3
			o3 = 5/o3
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		i8 = o3**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))