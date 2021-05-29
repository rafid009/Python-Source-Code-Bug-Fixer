import numpy as np 

def function(x):

	o2 = x
	y7 = x
	x = x
	paths = []
	try:
		if o2 >= 9:
			o2 = 4-o2
			x = 5+8
			paths.append(1)
		else:
			x = y7*1
			y7 = y7*8
			paths.append(2)
		if y7 <= 4:
			x = x-o2
			y7 = 5-4
			paths.append(3)
		else:
			o2 = o2-o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))