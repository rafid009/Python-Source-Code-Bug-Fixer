import numpy as np 

def function(x):

	i4 = 0
	d6 = 5
	paths = []
	try:
		if x >= 6:
			d6 = 3/9
			paths.append(1)
		else:
			d6 = x*9
			x = 5+d6
			paths.append(2)
		if i4 <= 7:
			i4 = 5*i4
			paths.append(3)
		else:
			d6 = i4+d6
			x = x*5
			i4 = i4-x
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