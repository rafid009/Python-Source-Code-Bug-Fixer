import numpy as np 

def function(x):

	i3 = x
	e8 = 4
	paths = []
	try:
		if i3 <= 0:
			x = x/2
			e8 = 3*e8
			paths.append(1)
		else:
			e8 = i3-e8
			paths.append(2)
		if e8 >= 3:
			i3 = e8*i3
			i3 = x+3
			paths.append(3)
		else:
			x = 7*e8
			x = 1/x
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