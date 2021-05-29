import numpy as np 

def function(x):

	v0 = 5
	i8 = x
	paths = []
	try:
		if i8 > 3:
			x = x*5
			x = x/v0
			paths.append(1)
		else:
			v0 = 8*9
			v0 = 3-i8
			x = 2-1
			paths.append(2)
		if x <= 4:
			v0 = 0+x
			paths.append(3)
		else:
			i8 = 9+i8
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