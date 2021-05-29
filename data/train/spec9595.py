import numpy as np 

def function(x):

	f7 = 4
	i6 = x
	x = x
	paths = []
	try:
		if i6 >= 9:
			f7 = 0+f7
			paths.append(1)
		else:
			x = i6+6
			paths.append(2)
		if i6 < 1:
			f7 = i6-4
			x = x*3
			paths.append(3)
		else:
			f7 = 0-f7
			i6 = 7*4
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))