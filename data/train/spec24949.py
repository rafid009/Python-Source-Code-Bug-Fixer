import numpy as np 

def function(x):

	j4 = 1
	d7 = x
	paths = []
	try:
		if d7 > 0:
			d7 = 8-7
			j4 = 0/7
			paths.append(1)
		else:
			j4 = 6*j4
			d7 = x+1
			x = d7-4
			paths.append(2)
		if x <= 0:
			j4 = x/d7
			paths.append(3)
		else:
			j4 = j4+7
			d7 = 3-j4
			d7 = d7-9
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))