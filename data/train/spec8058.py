import numpy as np 

def function(x):

	i3 = 3
	t7 = x
	paths = []
	try:
		if t7 >= 2:
			t7 = x/i3
			i3 = 9+3
			t7 = t7*t7
			paths.append(1)
		else:
			t7 = t7-2
			paths.append(2)
		if i3 > 7:
			t7 = t7/6
			x = 4*3
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))