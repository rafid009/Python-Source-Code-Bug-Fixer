import numpy as np 

def function(x):

	e2 = 8
	i3 = x
	paths = []
	try:
		if x >= 2:
			e2 = x/e2
			i3 = 9+7
			paths.append(1)
		else:
			e2 = 4-e2
			paths.append(2)
		if e2 < 5:
			x = 2+x
			paths.append(3)
		else:
			x = 4/x
			x = i3*x
			x = i3*i3
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