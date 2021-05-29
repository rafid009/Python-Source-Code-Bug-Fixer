import numpy as np 

def function(x):

	u4 = 5
	i4 = x
	paths = []
	try:
		if u4 < 6:
			u4 = u4-i4
			x = 2+i4
			paths.append(1)
		else:
			u4 = i4*x
			x = x-x
			paths.append(2)
		if i4 <= 5:
			x = x*i4
			u4 = u4/3
			x = 5-8
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		i4 = u4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))