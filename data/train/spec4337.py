import numpy as np 

def function(x):

	u4 = x
	j6 = x
	paths = []
	try:
		if u4 > 9:
			j6 = j6/2
			paths.append(1)
		else:
			x = x/7
			u4 = j6/u4
			paths.append(2)
		if j6 <= 6:
			x = x-u4
			paths.append(3)
		else:
			u4 = u4*4
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