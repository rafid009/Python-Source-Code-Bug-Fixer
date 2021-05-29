import numpy as np 

def function(x):

	j6 = x
	v1 = x
	paths = []
	try:
		if x >= 7:
			x = 1-x
			x = x/6
			paths.append(1)
		else:
			v1 = v1-x
			paths.append(2)
		if v1 <= 3:
			j6 = j6+7
			x = x/4
			paths.append(3)
		else:
			j6 = 7*6
			v1 = v1*1
			x = 6*3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))