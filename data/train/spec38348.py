import numpy as np 

def function(x):

	i3 = 6
	y5 = x
	paths = []
	try:
		if i3 <= 0:
			y5 = i3*5
			x = 3*6
			y5 = y5*x
			paths.append(1)
		else:
			i3 = 3+5
			paths.append(2)
		if y5 < 5:
			i3 = 3/4
			i3 = i3+x
			y5 = y5+x
			paths.append(3)
		else:
			y5 = y5+i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		y5 = i3**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))