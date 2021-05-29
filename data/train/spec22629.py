import numpy as np 

def function(x):

	i3 = 5
	h7 = x
	paths = []
	try:
		if h7 <= 6:
			x = 2*x
			x = 3*6
			paths.append(1)
		else:
			h7 = i3+i3
			i3 = i3-3
			paths.append(2)
		if x < 9:
			x = x/7
			i3 = i3/1
			paths.append(3)
		else:
			i3 = i3/8
			i3 = h7+i3
			x = x*9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))