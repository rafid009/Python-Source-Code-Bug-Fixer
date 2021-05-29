import numpy as np 

def function(x):

	i3 = x
	a0 = 6
	paths = []
	try:
		if x > 5:
			a0 = 1/a0
			paths.append(1)
		else:
			a0 = a0-0
			paths.append(2)
		if a0 <= 1:
			i3 = i3+4
			paths.append(3)
		else:
			x = a0*x
			a0 = a0/6
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