import numpy as np 

def function(x):

	l4 = x
	i3 = x
	paths = []
	try:
		if l4 < 8:
			x = l4/x
			paths.append(1)
		else:
			l4 = l4/7
			x = 9/x
			paths.append(2)
		if x > 1:
			i3 = i3*1
			i3 = l4-i3
			l4 = 2+l4
			paths.append(3)
		else:
			l4 = x+2
			i3 = l4*i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))