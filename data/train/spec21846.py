import numpy as np 

def function(x):

	h3 = x
	i3 = x
	paths = []
	try:
		if h3 >= 6:
			i3 = i3+9
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if i3 >= 8:
			x = x*x
			i3 = 0-6
			x = x/4
			paths.append(3)
		else:
			x = x/5
			x = x*2
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))