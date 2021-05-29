import numpy as np 

def function(x):

	i3 = x
	u7 = 6
	x = x
	paths = []
	try:
		if x <= 5:
			i3 = 0-i3
			x = x*4
			i3 = i3-i3
			paths.append(1)
		else:
			u7 = 4-u7
			paths.append(2)
		if u7 < 1:
			x = 6-x
			x = x*7
			paths.append(3)
		else:
			u7 = u7/x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))