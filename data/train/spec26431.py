import numpy as np 

def function(x):

	i9 = 5
	d4 = 6
	paths = []
	try:
		if i9 <= 6:
			d4 = d4-4
			i9 = i9/i9
			paths.append(1)
		else:
			x = 4/x
			d4 = 7-i9
			x = x/8
			paths.append(2)
		if x < 4:
			d4 = 7*i9
			x = x/4
			paths.append(3)
		else:
			x = x/i9
			d4 = d4+d4
			d4 = 0-d4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))