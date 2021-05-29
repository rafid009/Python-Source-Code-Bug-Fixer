import numpy as np 

def function(x):

	j6 = 4
	u7 = 9
	paths = []
	try:
		if u7 < 4:
			u7 = 8/u7
			paths.append(1)
		else:
			x = 1/x
			u7 = 6+x
			j6 = x+u7
			paths.append(2)
		if x < 2:
			u7 = u7/6
			j6 = j6-9
			paths.append(3)
		else:
			j6 = 3-6
			u7 = 2-u7
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