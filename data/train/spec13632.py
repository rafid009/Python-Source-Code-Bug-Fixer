import numpy as np 

def function(x):

	i6 = 8
	u4 = 1
	paths = []
	try:
		if u4 < 0:
			x = x*9
			paths.append(1)
		else:
			u4 = x/u4
			x = 9+u4
			paths.append(2)
		if i6 > 7:
			i6 = 0-i6
			x = 6-3
			i6 = i6*x
			paths.append(3)
		else:
			u4 = u4*x
			x = x*x
			x = x/5
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))