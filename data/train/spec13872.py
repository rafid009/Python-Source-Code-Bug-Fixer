import numpy as np 

def function(x):

	n6 = x
	i3 = 1
	paths = []
	try:
		if x > 4:
			i3 = 4/i3
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if x > 6:
			n6 = 2+n6
			paths.append(3)
		else:
			n6 = x*2
			i3 = 8/n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		i3 = n6**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))