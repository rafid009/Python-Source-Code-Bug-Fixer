import numpy as np 

def function(x):

	f9 = 3
	i8 = 5
	paths = []
	try:
		if x >= 1:
			x = x/1
			i8 = i8/1
			paths.append(1)
		else:
			x = 1+x
			i8 = 7-i8
			paths.append(2)
		if i8 > 9:
			f9 = x-i8
			paths.append(3)
		else:
			f9 = x*f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		i8 = f9**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))