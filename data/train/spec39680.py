import numpy as np 

def function(x):

	o9 = 8
	r6 = x
	paths = []
	try:
		if x >= 2:
			r6 = 9*r6
			r6 = o9+r6
			paths.append(1)
		else:
			x = x*3
			o9 = 0*o9
			o9 = 3/6
			paths.append(2)
		if x < 4:
			o9 = 6/o9
			o9 = o9-4
			o9 = o9+o9
			paths.append(3)
		else:
			o9 = o9*2
			x = r6*1
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))