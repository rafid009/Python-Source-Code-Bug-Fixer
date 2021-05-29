import numpy as np 

def function(x):

	i6 = 8
	i3 = x
	x = x
	paths = []
	try:
		if i6 < 1:
			x = x-x
			x = x/x
			paths.append(1)
		else:
			x = 2*i3
			i6 = i6*4
			paths.append(2)
		if i3 < 3:
			i6 = 1-i6
			paths.append(3)
		else:
			i3 = 4+5
			i3 = i3/1
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i6 = i3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))