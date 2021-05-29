import numpy as np 

def function(x):

	a9 = 8
	i4 = x
	paths = []
	try:
		if i4 > 9:
			i4 = i4+7
			paths.append(1)
		else:
			x = x*a9
			a9 = 6-a9
			a9 = a9*i4
			paths.append(2)
		if x < 7:
			a9 = a9*9
			paths.append(3)
		else:
			i4 = 4+i4
			a9 = 8-a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		i4 = a9**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))