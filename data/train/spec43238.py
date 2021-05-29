import numpy as np 

def function(x):

	i8 = x
	o5 = 7
	paths = []
	try:
		if o5 >= 3:
			x = x-5
			paths.append(1)
		else:
			o5 = o5*i8
			o5 = i8+7
			o5 = o5+4
			paths.append(2)
		if i8 <= 8:
			x = x-4
			o5 = i8+o5
			i8 = i8-x
			paths.append(3)
		else:
			i8 = 0-i8
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		i8 = o5**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))