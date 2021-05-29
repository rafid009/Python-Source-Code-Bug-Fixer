import numpy as np 

def function(x):

	a4 = x
	i3 = 8
	paths = []
	try:
		if i3 > 9:
			i3 = 6+i3
			a4 = a4-x
			i3 = i3-i3
			paths.append(1)
		else:
			i3 = x/8
			x = i3*3
			paths.append(2)
		if x > 9:
			i3 = i3*6
			paths.append(3)
		else:
			a4 = a4+a4
			i3 = a4/a4
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