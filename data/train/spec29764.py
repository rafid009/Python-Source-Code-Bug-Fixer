import numpy as np 

def function(x):

	i3 = x
	s0 = 2
	paths = []
	try:
		if i3 > 6:
			x = 8-x
			paths.append(1)
		else:
			s0 = 6/6
			paths.append(2)
		if i3 >= 1:
			x = x+s0
			i3 = 6+7
			i3 = 4+i3
			paths.append(3)
		else:
			s0 = s0-7
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