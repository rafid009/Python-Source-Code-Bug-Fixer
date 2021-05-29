import numpy as np 

def function(x):

	u6 = x
	i8 = 6
	paths = []
	try:
		if i8 >= 1:
			x = u6+8
			u6 = u6-5
			u6 = u6+u6
			paths.append(1)
		else:
			u6 = u6-5
			u6 = x/3
			paths.append(2)
		if x < 3:
			x = u6/x
			x = 6/x
			i8 = 8*i8
			paths.append(3)
		else:
			u6 = i8+9
			u6 = u6-u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))