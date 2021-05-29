import numpy as np 

def function(x):

	i3 = x
	l4 = 5
	x = 0
	paths = []
	try:
		if x > 9:
			i3 = l4/i3
			l4 = 7-4
			paths.append(1)
		else:
			i3 = i3/2
			x = 0+2
			paths.append(2)
		if x < 6:
			i3 = 4-i3
			i3 = i3-x
			x = x/i3
			paths.append(3)
		else:
			i3 = i3*0
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		l4 = i3**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))