import numpy as np 

def function(x):

	i5 = x
	o7 = x
	paths = []
	try:
		if o7 > 3:
			o7 = o7/1
			i5 = i5/i5
			o7 = 0/3
			paths.append(1)
		else:
			i5 = 0/i5
			paths.append(2)
		if i5 <= 0:
			i5 = 3+0
			paths.append(3)
		else:
			o7 = 2*4
			i5 = i5*6
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		i5 = o7**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))