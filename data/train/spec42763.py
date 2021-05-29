import numpy as np 

def function(x):

	j3 = 0
	o9 = 3
	x = x
	paths = []
	try:
		if x > 4:
			x = x*7
			o9 = 6/o9
			paths.append(1)
		else:
			j3 = j3+6
			j3 = o9/j3
			o9 = 6/o9
			paths.append(2)
		if o9 > 8:
			o9 = o9*o9
			x = x/7
			j3 = 3+8
			paths.append(3)
		else:
			j3 = j3-9
			o9 = x/o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))