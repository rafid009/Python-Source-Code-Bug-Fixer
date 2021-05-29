import numpy as np 

def function(x):

	a9 = x
	v4 = x
	paths = []
	try:
		if a9 <= 5:
			v4 = v4+a9
			v4 = 4*6
			x = 3+2
			paths.append(1)
		else:
			v4 = 3-6
			a9 = 5/a9
			v4 = 2/a9
			paths.append(2)
		if v4 >= 2:
			v4 = v4+7
			paths.append(3)
		else:
			x = 0-x
			x = x-1
			x = 1*8
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))