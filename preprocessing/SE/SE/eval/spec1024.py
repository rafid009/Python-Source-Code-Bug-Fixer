import numpy as np 

def function(x):

	v3 = 0
	j9 = 2
	x = x
	paths = []
	try:
		if v3 <= 5:
			v3 = x+v3
			v3 = 8*8
			paths.append(1)
		else:
			v3 = x-v3
			j9 = 6-j9
			paths.append(2)
		if x >= 1:
			v3 = x-6
			v3 = v3+v3
			paths.append(3)
		else:
			v3 = 8*v3
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