import numpy as np 

def function(x):

	j6 = 6
	k5 = 4
	paths = []
	try:
		if x >= 8:
			j6 = 3*4
			k5 = k5*4
			paths.append(1)
		else:
			j6 = 2+j6
			j6 = k5+4
			k5 = 6/3
			paths.append(2)
		if k5 >= 1:
			j6 = 2+j6
			paths.append(3)
		else:
			x = 3+7
			k5 = 9*k5
			j6 = j6*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))