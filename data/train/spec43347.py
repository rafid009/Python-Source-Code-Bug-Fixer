import numpy as np 

def function(x):

	j6 = 2
	a9 = 9
	paths = []
	try:
		if j6 > 8:
			a9 = 2/a9
			a9 = a9/8
			a9 = j6+8
			paths.append(1)
		else:
			a9 = a9-a9
			x = 9*x
			paths.append(2)
		if a9 > 8:
			a9 = a9*6
			j6 = j6*a9
			paths.append(3)
		else:
			a9 = 5-x
			j6 = j6+7
			a9 = a9/4
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		j6 = a9**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))