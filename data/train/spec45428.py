import numpy as np 

def function(x):

	l6 = 3
	i3 = x
	paths = []
	try:
		if i3 >= 7:
			x = i3/8
			i3 = l6-i3
			paths.append(1)
		else:
			i3 = i3/4
			paths.append(2)
		if i3 < 6:
			l6 = l6/l6
			x = x*5
			paths.append(3)
		else:
			i3 = x*1
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