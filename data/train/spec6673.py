import numpy as np 

def function(x):

	i3 = x
	paths = []
	try:
		if x >= 8:
			x = x*9
			paths.append(1)
		else:
			i3 = i3-6
			i3 = 1+x
			paths.append(2)
		if x <= 7:
			x = x/i3
			paths.append(3)
		else:
			i3 = i3+x
			x = 2+x
			i3 = i3*6
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