import numpy as np 

def function(x):

	x9 = x
	i8 = x
	paths = []
	try:
		if i8 <= 9:
			x = x+x9
			paths.append(1)
		else:
			i8 = 8+i8
			paths.append(2)
		if x > 6:
			x9 = x9/i8
			x = 2+7
			paths.append(3)
		else:
			x9 = x9*0
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