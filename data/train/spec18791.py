import numpy as np 

def function(x):

	j4 = 8
	d1 = 1
	paths = []
	try:
		if x < 7:
			j4 = j4-5
			j4 = 0/4
			paths.append(1)
		else:
			d1 = d1/j4
			x = j4-x
			paths.append(2)
		if j4 < 9:
			d1 = d1+x
			d1 = 0+d1
			j4 = j4+9
			paths.append(3)
		else:
			d1 = 2*j4
			j4 = j4+9
			d1 = x-0
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))