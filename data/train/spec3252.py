import numpy as np 

def function(x):

	f8 = 3
	i3 = x
	paths = []
	try:
		if x <= 1:
			f8 = f8/3
			x = x-6
			i3 = x/i3
			paths.append(1)
		else:
			i3 = i3-0
			f8 = 6+f8
			paths.append(2)
		if f8 < 3:
			f8 = 4-f8
			paths.append(3)
		else:
			f8 = x-f8
			f8 = 1/4
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