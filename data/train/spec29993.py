import numpy as np 

def function(x):

	i6 = x
	d7 = 9
	paths = []
	try:
		if i6 >= 2:
			d7 = 6/1
			x = 5+4
			d7 = d7-8
			paths.append(1)
		else:
			i6 = i6+7
			i6 = i6*d7
			d7 = d7+0
			paths.append(2)
		if d7 < 5:
			i6 = i6+2
			x = x*3
			x = d7-i6
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		i6 = d7**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))