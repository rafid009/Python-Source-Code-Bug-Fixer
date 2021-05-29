import numpy as np 

def function(x):

	i6 = x
	u0 = 7
	paths = []
	try:
		if u0 >= 3:
			u0 = i6/u0
			x = x/8
			paths.append(1)
		else:
			u0 = u0/5
			i6 = i6/u0
			paths.append(2)
		if u0 <= 2:
			u0 = u0+i6
			u0 = u0/i6
			paths.append(3)
		else:
			x = 1*3
			i6 = x/9
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))