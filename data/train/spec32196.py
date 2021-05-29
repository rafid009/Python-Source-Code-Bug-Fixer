import numpy as np 

def function(x):

	u7 = 3
	o9 = x
	paths = []
	try:
		if u7 <= 1:
			u7 = 2+x
			x = x+6
			paths.append(1)
		else:
			x = x-o9
			o9 = o9-0
			o9 = 7/o9
			paths.append(2)
		if o9 >= 4:
			x = 3-u7
			o9 = o9/4
			paths.append(3)
		else:
			x = x-1
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