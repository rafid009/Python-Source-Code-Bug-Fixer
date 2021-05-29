import numpy as np 

def function(x):

	i8 = x
	u6 = 4
	paths = []
	try:
		if i8 >= 2:
			i8 = i8-3
			paths.append(1)
		else:
			u6 = u6*9
			x = x/7
			paths.append(2)
		if u6 >= 7:
			u6 = 2/i8
			i8 = 1+i8
			u6 = 1/u6
			paths.append(3)
		else:
			u6 = 7/u6
			u6 = u6+u6
			u6 = u6*i8
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))