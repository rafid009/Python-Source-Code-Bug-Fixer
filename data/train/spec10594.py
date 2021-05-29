import numpy as np 

def function(x):

	v2 = x
	o9 = 9
	paths = []
	try:
		if x > 9:
			v2 = 0+x
			paths.append(1)
		else:
			o9 = x-o9
			paths.append(2)
		if o9 > 5:
			v2 = x/1
			o9 = o9+o9
			x = 3+x
			paths.append(3)
		else:
			x = v2-x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))