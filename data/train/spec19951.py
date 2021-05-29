import numpy as np 

def function(x):

	d5 = x
	i6 = x
	paths = []
	try:
		if i6 < 0:
			x = x-2
			paths.append(1)
		else:
			d5 = 7*d5
			i6 = 2+i6
			i6 = i6*3
			paths.append(2)
		if i6 <= 0:
			x = x+4
			x = d5/1
			paths.append(3)
		else:
			d5 = d5/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		d5 = i6**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))