import numpy as np 

def function(x):

	j4 = 8
	d1 = x
	paths = []
	try:
		if d1 >= 1:
			d1 = 1-1
			j4 = j4*j4
			x = d1/9
			paths.append(1)
		else:
			j4 = j4-8
			x = x-5
			d1 = d1/3
			paths.append(2)
		if d1 > 4:
			x = 2/1
			paths.append(3)
		else:
			j4 = j4-0
			x = 9-x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))