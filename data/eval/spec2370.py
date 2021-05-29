import numpy as np 

def function(x):

	i3 = 9
	x6 = x
	paths = []
	try:
		if x6 >= 5:
			x = 2*7
			paths.append(1)
		else:
			i3 = i3*3
			x = x/6
			paths.append(2)
		if i3 >= 9:
			x = x-2
			i3 = 2/x
			paths.append(3)
		else:
			x6 = 1*3
			x = i3-7
			x6 = x6/x6
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))