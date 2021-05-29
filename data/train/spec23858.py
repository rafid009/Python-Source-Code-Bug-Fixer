import numpy as np 

def function(x):

	j5 = x
	i8 = 3
	paths = []
	try:
		if x < 1:
			i8 = i8/6
			x = 3/x
			paths.append(1)
		else:
			i8 = i8*1
			j5 = 7-3
			paths.append(2)
		if i8 < 7:
			j5 = j5/6
			i8 = i8/2
			paths.append(3)
		else:
			i8 = i8-i8
			j5 = 0*1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))