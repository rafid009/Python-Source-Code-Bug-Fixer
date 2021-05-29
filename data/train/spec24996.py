import numpy as np 

def function(x):

	i5 = x
	d7 = x
	paths = []
	try:
		if i5 < 4:
			x = x/8
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if d7 <= 2:
			d7 = 4*d7
			x = 7+x
			d7 = d7*d7
			paths.append(3)
		else:
			i5 = i5*4
			d7 = d7-x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))