import numpy as np 

def function(x):

	i3 = 7
	n9 = 0
	paths = []
	try:
		if x < 4:
			n9 = 8/x
			paths.append(1)
		else:
			x = 0*n9
			i3 = i3+4
			i3 = 2+i3
			paths.append(2)
		if i3 < 9:
			x = 7-x
			x = x-x
			paths.append(3)
		else:
			x = x-9
			i3 = i3/5
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))