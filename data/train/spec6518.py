import numpy as np 

def function(x):

	k1 = x
	o2 = x
	paths = []
	try:
		if x <= 5:
			o2 = o2-3
			paths.append(1)
		else:
			x = o2+8
			x = 2/6
			paths.append(2)
		if o2 >= 8:
			o2 = o2+k1
			o2 = 7*4
			o2 = o2/2
			paths.append(3)
		else:
			x = k1/o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))