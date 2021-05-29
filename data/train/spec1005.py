import numpy as np 

def function(x):

	u3 = x
	i3 = 2
	paths = []
	try:
		if u3 >= 9:
			x = x-i3
			paths.append(1)
		else:
			u3 = u3*4
			i3 = i3/4
			x = x+x
			paths.append(2)
		if i3 < 9:
			u3 = 4*6
			u3 = i3/i3
			paths.append(3)
		else:
			i3 = i3/i3
			i3 = i3/u3
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