import numpy as np 

def function(x):

	u4 = x
	j4 = 8
	paths = []
	try:
		if u4 <= 9:
			j4 = j4+5
			u4 = 1+4
			j4 = j4-4
			paths.append(1)
		else:
			x = 4+x
			u4 = u4/j4
			j4 = j4-5
			paths.append(2)
		if j4 <= 5:
			x = j4+1
			x = x-0
			u4 = u4-5
			paths.append(3)
		else:
			u4 = 1-5
			u4 = u4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))