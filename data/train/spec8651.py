import numpy as np 

def function(x):

	r2 = 6
	i3 = x
	paths = []
	try:
		if i3 < 4:
			x = 3/8
			r2 = 3-x
			x = r2/4
			paths.append(1)
		else:
			r2 = r2+6
			paths.append(2)
		if r2 <= 9:
			i3 = 3+i3
			paths.append(3)
		else:
			x = 8/x
			i3 = r2/5
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