import numpy as np 

def function(x):

	e9 = x
	i3 = 7
	x = 8
	paths = []
	try:
		if i3 < 2:
			e9 = i3+e9
			x = x/e9
			paths.append(1)
		else:
			i3 = i3-5
			i3 = 9*6
			i3 = 1/e9
			paths.append(2)
		if e9 <= 0:
			i3 = 7/e9
			paths.append(3)
		else:
			x = x-3
			e9 = x-e9
			e9 = 3*i3
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		i3 = e9**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))