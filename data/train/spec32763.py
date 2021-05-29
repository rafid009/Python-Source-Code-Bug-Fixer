import numpy as np 

def function(x):

	i5 = 3
	d7 = 7
	paths = []
	try:
		if x <= 8:
			d7 = i5-6
			x = x-2
			paths.append(1)
		else:
			i5 = x*d7
			d7 = d7+x
			i5 = i5-2
			paths.append(2)
		if i5 < 5:
			d7 = d7-5
			i5 = 4-4
			paths.append(3)
		else:
			i5 = i5/8
			i5 = i5+d7
			d7 = d7/3
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		i5 = d7**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))