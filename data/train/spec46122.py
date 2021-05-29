import numpy as np 

def function(x):

	d2 = 2
	j1 = x
	paths = []
	try:
		if d2 < 0:
			x = 7/x
			j1 = d2/4
			paths.append(1)
		else:
			d2 = x-d2
			d2 = 7-d2
			paths.append(2)
		if j1 <= 3:
			j1 = 4/j1
			paths.append(3)
		else:
			x = x*6
			d2 = d2/8
			j1 = j1/9
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		d2 = j1**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))