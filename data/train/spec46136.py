import numpy as np 

def function(x):

	i7 = 4
	v2 = 5
	x = x
	paths = []
	try:
		if i7 <= 0:
			x = v2+x
			v2 = 9/v2
			x = 7/v2
			paths.append(1)
		else:
			i7 = v2*v2
			v2 = 6-v2
			paths.append(2)
		if x >= 7:
			v2 = 5/x
			i7 = 2-i7
			i7 = i7+i7
			paths.append(3)
		else:
			i7 = i7+0
			v2 = v2*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))