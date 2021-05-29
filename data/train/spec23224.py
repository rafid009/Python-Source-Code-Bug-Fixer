import numpy as np 

def function(x):

	i5 = x
	v5 = 2
	paths = []
	try:
		if i5 <= 9:
			v5 = 9+v5
			x = v5*x
			paths.append(1)
		else:
			i5 = i5-2
			x = 9*x
			paths.append(2)
		if i5 >= 7:
			i5 = 5-i5
			i5 = 9/i5
			i5 = i5*3
			paths.append(3)
		else:
			i5 = 8-0
			x = 3/5
			i5 = 7/2
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		v5 = i5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))