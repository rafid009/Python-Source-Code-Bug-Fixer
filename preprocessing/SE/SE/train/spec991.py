import numpy as np 

def function(x):

	u6 = x
	j4 = x
	paths = []
	try:
		if j4 > 9:
			u6 = u6-j4
			x = 6/x
			x = x-4
			paths.append(1)
		else:
			u6 = j4*2
			paths.append(2)
		if u6 > 2:
			x = x-8
			paths.append(3)
		else:
			j4 = u6+5
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))