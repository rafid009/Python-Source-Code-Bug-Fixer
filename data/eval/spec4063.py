import numpy as np 

def function(x):

	i9 = x
	u4 = 2
	paths = []
	try:
		if u4 >= 0:
			x = x/5
			i9 = i9/7
			paths.append(1)
		else:
			i9 = i9-i9
			u4 = 5/u4
			paths.append(2)
		if i9 > 2:
			x = 4*x
			i9 = i9-x
			x = x*i9
			paths.append(3)
		else:
			i9 = 8-x
			x = u4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))