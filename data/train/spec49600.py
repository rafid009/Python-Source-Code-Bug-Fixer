import numpy as np 

def function(x):

	i3 = x
	d2 = 3
	paths = []
	try:
		if d2 <= 6:
			i3 = i3+d2
			d2 = d2/6
			d2 = d2+7
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x > 2:
			i3 = i3-5
			d2 = i3+i3
			x = 3*x
			paths.append(3)
		else:
			x = i3-x
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