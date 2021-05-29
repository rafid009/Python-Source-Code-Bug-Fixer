import numpy as np 

def function(x):

	a2 = 4
	i3 = x
	paths = []
	try:
		if i3 <= 4:
			a2 = a2-a2
			paths.append(1)
		else:
			i3 = a2-i3
			paths.append(2)
		if i3 > 9:
			i3 = 9+3
			i3 = 0+5
			paths.append(3)
		else:
			x = 6+x
			i3 = 9/i3
			i3 = i3+4
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