import numpy as np 

def function(x):

	v2 = x
	j9 = 3
	paths = []
	try:
		if x < 9:
			j9 = 8+j9
			j9 = 4-6
			paths.append(1)
		else:
			x = 9-8
			v2 = 9*v2
			v2 = 4-v2
			paths.append(2)
		if j9 < 0:
			j9 = j9-4
			j9 = j9*4
			paths.append(3)
		else:
			v2 = 4+x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))