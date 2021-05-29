import numpy as np 

def function(x):

	k7 = 3
	j6 = x
	paths = []
	try:
		if x >= 1:
			j6 = j6/7
			x = j6*9
			paths.append(1)
		else:
			x = k7-8
			paths.append(2)
		if x < 3:
			k7 = j6-k7
			x = 9/x
			paths.append(3)
		else:
			x = x*3
			k7 = k7/5
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))