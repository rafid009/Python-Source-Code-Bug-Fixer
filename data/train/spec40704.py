import numpy as np 

def function(x):

	t0 = 1
	i3 = x
	paths = []
	try:
		if i3 < 5:
			t0 = 3-2
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if i3 > 7:
			x = 7+i3
			x = x+0
			paths.append(3)
		else:
			t0 = t0-5
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