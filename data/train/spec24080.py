import numpy as np 

def function(x):

	i5 = 7
	u7 = 8
	x = x
	paths = []
	try:
		if x >= 4:
			i5 = i5*3
			paths.append(1)
		else:
			i5 = 6-i5
			paths.append(2)
		if i5 < 7:
			x = 3*x
			u7 = 5*3
			paths.append(3)
		else:
			u7 = u7-u7
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))