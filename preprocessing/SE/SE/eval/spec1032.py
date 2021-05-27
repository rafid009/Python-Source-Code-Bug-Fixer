import numpy as np 

def function(x):

	i3 = 2
	l5 = 9
	paths = []
	try:
		if x > 0:
			i3 = i3*l5
			x = 5-2
			paths.append(1)
		else:
			l5 = 8-l5
			l5 = l5/l5
			paths.append(2)
		if l5 >= 1:
			i3 = l5*1
			x = 4*i3
			i3 = 2-i3
			paths.append(3)
		else:
			x = x/l5
			i3 = 4*3
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