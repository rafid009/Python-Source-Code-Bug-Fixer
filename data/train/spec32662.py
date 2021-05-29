import numpy as np 

def function(x):

	j2 = 8
	i3 = x
	paths = []
	try:
		if x >= 0:
			x = 5+i3
			j2 = i3/j2
			paths.append(1)
		else:
			i3 = i3+8
			paths.append(2)
		if j2 > 5:
			i3 = i3+4
			i3 = i3+7
			paths.append(3)
		else:
			x = 5/x
			i3 = 6-i3
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