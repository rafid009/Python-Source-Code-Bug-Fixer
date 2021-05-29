import numpy as np 

def function(x):

	d9 = 9
	i3 = 8
	paths = []
	try:
		if x >= 9:
			i3 = i3*5
			paths.append(1)
		else:
			d9 = d9-4
			i3 = d9-i3
			paths.append(2)
		if x <= 5:
			d9 = i3*d9
			i3 = d9+i3
			d9 = 7+d9
			paths.append(3)
		else:
			i3 = x-x
			x = 3+d9
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