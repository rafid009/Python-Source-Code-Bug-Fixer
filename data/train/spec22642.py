import numpy as np 

def function(x):

	g9 = 9
	i3 = x
	paths = []
	try:
		if x >= 3:
			i3 = i3*i3
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x < 6:
			g9 = 5/g9
			g9 = i3+i3
			paths.append(3)
		else:
			g9 = g9-x
			i3 = 0/i3
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		i3 = g9**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))