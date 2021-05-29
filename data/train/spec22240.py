import numpy as np 

def function(x):

	f3 = 4
	i4 = x
	paths = []
	try:
		if x > 2:
			f3 = f3*5
			x = x-5
			paths.append(1)
		else:
			f3 = 8*6
			x = 0-x
			paths.append(2)
		if f3 < 2:
			f3 = 5-f3
			i4 = 1/9
			i4 = i4*i4
			paths.append(3)
		else:
			f3 = i4-f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))