import numpy as np 

def function(x):

	i3 = 1
	j4 = x
	paths = []
	try:
		if x > 7:
			j4 = j4+5
			paths.append(1)
		else:
			i3 = 5/j4
			j4 = 9*9
			paths.append(2)
		if x > 5:
			i3 = i3/i3
			x = x-2
			paths.append(3)
		else:
			i3 = i3+5
			j4 = i3*j4
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))