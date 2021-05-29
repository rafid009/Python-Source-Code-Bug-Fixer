import numpy as np 

def function(x):

	i3 = 0
	p1 = x
	paths = []
	try:
		if i3 > 8:
			i3 = i3-9
			i3 = i3-7
			paths.append(1)
		else:
			i3 = 7-i3
			i3 = p1-1
			i3 = 2*i3
			paths.append(2)
		if i3 > 0:
			x = 1-x
			paths.append(3)
		else:
			i3 = x*i3
			x = x-7
			p1 = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))