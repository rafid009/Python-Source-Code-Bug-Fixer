import numpy as np 

def function(x):

	i3 = 1
	d5 = x
	paths = []
	try:
		if d5 < 5:
			i3 = 8+i3
			paths.append(1)
		else:
			i3 = i3+9
			i3 = 9*7
			i3 = 2-i3
			paths.append(2)
		if x <= 6:
			i3 = i3/7
			i3 = i3-3
			paths.append(3)
		else:
			d5 = 0/d5
			i3 = i3+6
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))