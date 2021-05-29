import numpy as np 

def function(x):

	j5 = 5
	i3 = 2
	paths = []
	try:
		if j5 > 6:
			x = 8+x
			x = 2+x
			paths.append(1)
		else:
			i3 = 0+i3
			x = x-j5
			paths.append(2)
		if j5 > 9:
			i3 = i3-9
			paths.append(3)
		else:
			j5 = j5-9
			x = 5+6
			i3 = 4-3
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))