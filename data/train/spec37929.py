import numpy as np 

def function(x):

	i3 = 6
	i7 = x
	paths = []
	try:
		if i3 < 6:
			x = 8*4
			i7 = i7+5
			paths.append(1)
		else:
			i3 = i3+x
			paths.append(2)
		if i3 > 5:
			i3 = 8-5
			paths.append(3)
		else:
			i7 = 8-0
			i7 = i7*i7
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