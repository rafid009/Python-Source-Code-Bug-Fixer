import numpy as np 

def function(x):

	i9 = 3
	i3 = 8
	paths = []
	try:
		if x <= 8:
			i9 = 1+i9
			i3 = i9-x
			i9 = i9*i9
			paths.append(1)
		else:
			i9 = 0+1
			i9 = 4-i9
			x = x+1
			paths.append(2)
		if i9 > 8:
			i3 = i3*7
			x = x+i9
			paths.append(3)
		else:
			x = i3-4
			i3 = 7*5
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