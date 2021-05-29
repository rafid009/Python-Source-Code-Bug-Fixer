import numpy as np 

def function(x):

	j6 = 5
	d0 = x
	paths = []
	try:
		if d0 >= 5:
			j6 = 0-j6
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if j6 > 6:
			x = 3+x
			x = 5/x
			paths.append(3)
		else:
			d0 = 0+8
			d0 = d0*1
			j6 = 7/j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		d0 = j6**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))