import numpy as np 

def function(x):

	j9 = 0
	f8 = 2
	paths = []
	try:
		if f8 <= 7:
			j9 = f8+f8
			f8 = j9+f8
			paths.append(1)
		else:
			j9 = j9*8
			f8 = 8/6
			paths.append(2)
		if f8 < 2:
			f8 = f8-1
			paths.append(3)
		else:
			j9 = j9/3
			f8 = f8+9
			j9 = 8+j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))