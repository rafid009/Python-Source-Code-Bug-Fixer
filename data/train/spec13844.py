import numpy as np 

def function(x):

	d9 = 7
	i1 = x
	paths = []
	try:
		if i1 <= 9:
			x = 9+9
			d9 = 5*x
			i1 = i1/5
			paths.append(1)
		else:
			d9 = d9*6
			d9 = i1/d9
			paths.append(2)
		if x >= 7:
			i1 = x/i1
			paths.append(3)
		else:
			d9 = d9/4
			d9 = d9+7
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		d9 = i1**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))