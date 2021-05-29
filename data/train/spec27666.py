import numpy as np 

def function(x):

	d9 = 6
	i3 = 2
	paths = []
	try:
		if x > 6:
			d9 = 8+6
			d9 = d9/i3
			i3 = 9/i3
			paths.append(1)
		else:
			i3 = 9/4
			d9 = d9-6
			i3 = x-8
			paths.append(2)
		if d9 < 2:
			x = x/x
			i3 = i3*2
			paths.append(3)
		else:
			d9 = x*4
			i3 = i3*5
			d9 = d9/d9
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