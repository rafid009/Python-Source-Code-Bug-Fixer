import numpy as np 

def function(x):

	i3 = 6
	p1 = 0
	paths = []
	try:
		if i3 > 3:
			p1 = x-1
			paths.append(1)
		else:
			p1 = i3+i3
			i3 = 5-i3
			i3 = x/x
			paths.append(2)
		if x > 6:
			i3 = i3-1
			i3 = i3*6
			i3 = 8-i3
			paths.append(3)
		else:
			i3 = i3-8
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