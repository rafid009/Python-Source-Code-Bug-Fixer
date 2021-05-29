import numpy as np 

def function(x):

	o6 = x
	j2 = x
	paths = []
	try:
		if x >= 8:
			x = o6-3
			o6 = o6-4
			paths.append(1)
		else:
			j2 = j2/7
			x = 3-6
			paths.append(2)
		if x < 6:
			j2 = j2+1
			o6 = o6+o6
			paths.append(3)
		else:
			j2 = x/j2
			j2 = j2-4
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))