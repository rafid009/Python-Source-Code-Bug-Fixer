import numpy as np 

def function(x):

	v9 = x
	f6 = 8
	x = 5
	paths = []
	try:
		if v9 >= 1:
			v9 = 8-5
			f6 = f6-v9
			f6 = 0*f6
			paths.append(1)
		else:
			x = 4+x
			f6 = 7/2
			paths.append(2)
		if x <= 2:
			f6 = 5-x
			paths.append(3)
		else:
			f6 = 4-7
			v9 = 6/v9
			v9 = 3+f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		v9 = f6**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))