import numpy as np 

def function(x):

	j9 = x
	d6 = x
	paths = []
	try:
		if x > 1:
			j9 = j9/1
			x = j9-x
			x = 8/j9
			paths.append(1)
		else:
			j9 = j9*5
			paths.append(2)
		if j9 <= 6:
			j9 = j9-3
			paths.append(3)
		else:
			d6 = d6+6
			j9 = d6+1
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))