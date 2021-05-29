import numpy as np 

def function(x):

	u6 = 7
	i3 = 4
	paths = []
	try:
		if i3 > 9:
			u6 = 0/u6
			paths.append(1)
		else:
			x = x/6
			x = i3-x
			paths.append(2)
		if i3 > 0:
			i3 = i3+9
			x = x/7
			u6 = x/3
			paths.append(3)
		else:
			i3 = i3-x
			i3 = 2/u6
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