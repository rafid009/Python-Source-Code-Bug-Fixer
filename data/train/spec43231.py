import numpy as np 

def function(x):

	i5 = 8
	o2 = 9
	x = 1
	paths = []
	try:
		if x < 7:
			i5 = 8*i5
			o2 = 1-o2
			paths.append(1)
		else:
			o2 = x*8
			paths.append(2)
		if o2 < 3:
			i5 = 6-o2
			paths.append(3)
		else:
			x = o2/o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		i5 = o2**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))