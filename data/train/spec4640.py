import numpy as np 

def function(x):

	u6 = x
	i3 = x
	paths = []
	try:
		if i3 >= 5:
			i3 = i3/x
			paths.append(1)
		else:
			x = 6+x
			u6 = 4+u6
			x = u6*7
			paths.append(2)
		if i3 < 7:
			u6 = i3*u6
			paths.append(3)
		else:
			u6 = 3+4
			u6 = u6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))