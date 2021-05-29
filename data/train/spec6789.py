import numpy as np 

def function(x):

	j6 = x
	a0 = 8
	paths = []
	try:
		if a0 < 2:
			x = x-2
			paths.append(1)
		else:
			j6 = 1+9
			paths.append(2)
		if a0 > 6:
			a0 = 1-a0
			paths.append(3)
		else:
			x = x+a0
			j6 = 9-x
			x = j6+a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		j6 = a0**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))