import numpy as np 

def function(x):

	o9 = 4
	i5 = x
	paths = []
	try:
		if x >= 4:
			i5 = i5+i5
			i5 = i5+x
			x = x*9
			paths.append(1)
		else:
			o9 = i5-o9
			paths.append(2)
		if i5 < 9:
			o9 = 5-o9
			o9 = 3-7
			i5 = 4+x
			paths.append(3)
		else:
			i5 = o9/i5
			i5 = i5-3
			x = x*6
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