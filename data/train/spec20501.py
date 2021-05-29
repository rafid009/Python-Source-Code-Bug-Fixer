import numpy as np 

def function(x):

	t6 = x
	i3 = 7
	paths = []
	try:
		if t6 > 4:
			i3 = i3/i3
			x = 4-1
			x = 8-6
			paths.append(1)
		else:
			i3 = 5-i3
			x = x/3
			paths.append(2)
		if i3 < 4:
			i3 = i3*9
			paths.append(3)
		else:
			i3 = 9-i3
			x = x+i3
			x = x-4
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