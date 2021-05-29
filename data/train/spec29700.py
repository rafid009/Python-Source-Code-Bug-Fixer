import numpy as np 

def function(x):

	f6 = x
	j6 = 9
	paths = []
	try:
		if j6 >= 1:
			f6 = 2*f6
			j6 = 4+8
			f6 = f6-1
			paths.append(1)
		else:
			f6 = f6+0
			j6 = 7*f6
			paths.append(2)
		if x <= 6:
			j6 = j6/8
			x = x-7
			f6 = 3-f6
			paths.append(3)
		else:
			x = j6*f6
			f6 = f6+5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))