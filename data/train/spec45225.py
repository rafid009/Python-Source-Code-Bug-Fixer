import numpy as np 

def function(x):

	o9 = x
	j8 = x
	x = x
	paths = []
	try:
		if o9 <= 8:
			x = x-2
			j8 = o9/5
			j8 = j8/o9
			paths.append(1)
		else:
			o9 = 1*o9
			x = 8*7
			o9 = o9/8
			paths.append(2)
		if o9 < 4:
			j8 = j8/7
			j8 = j8-o9
			j8 = 8*j8
			paths.append(3)
		else:
			x = 8*j8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		o9 = j8**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))