import numpy as np 

def function(x):

	o2 = 2
	i6 = 8
	paths = []
	try:
		if i6 < 8:
			o2 = i6-o2
			x = 8+3
			o2 = 6/o2
			paths.append(1)
		else:
			o2 = i6*3
			i6 = x/i6
			paths.append(2)
		if o2 > 3:
			x = 6*x
			paths.append(3)
		else:
			o2 = o2-i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))