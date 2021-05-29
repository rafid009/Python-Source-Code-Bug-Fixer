import numpy as np 

def function(x):

	u6 = 0
	i6 = x
	paths = []
	try:
		if i6 <= 9:
			i6 = 6*i6
			paths.append(1)
		else:
			i6 = x-6
			i6 = i6*7
			paths.append(2)
		if i6 > 4:
			x = i6-x
			u6 = 5+u6
			i6 = 1-i6
			paths.append(3)
		else:
			u6 = 1*u6
			x = 6+i6
			i6 = 9-i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))