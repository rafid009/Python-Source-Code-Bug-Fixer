import numpy as np 

def function(x):

	k1 = x
	o7 = 2
	paths = []
	try:
		if x > 5:
			o7 = o7*k1
			paths.append(1)
		else:
			o7 = o7+8
			o7 = 4*o7
			paths.append(2)
		if k1 < 4:
			o7 = o7/7
			paths.append(3)
		else:
			o7 = x-7
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))