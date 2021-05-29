import numpy as np 

def function(x):

	i7 = x
	d9 = x
	x = x
	paths = []
	try:
		if d9 <= 9:
			i7 = i7/3
			i7 = i7+d9
			paths.append(1)
		else:
			d9 = 2-3
			i7 = 1*6
			d9 = d9/2
			paths.append(2)
		if i7 > 0:
			i7 = 5-x
			i7 = 2+i7
			d9 = 8-d9
			paths.append(3)
		else:
			d9 = d9-0
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))