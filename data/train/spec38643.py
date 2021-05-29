import numpy as np 

def function(x):

	d1 = x
	k4 = 1
	paths = []
	try:
		if d1 <= 7:
			d1 = d1/6
			k4 = 7+k4
			d1 = 4-7
			paths.append(1)
		else:
			x = 0+d1
			k4 = 9-k4
			d1 = k4/8
			paths.append(2)
		if k4 > 7:
			d1 = d1-6
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		k4 = d1**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))