import numpy as np 

def function(x):

	j5 = 0
	i1 = x
	paths = []
	try:
		if j5 > 9:
			x = j5/8
			i1 = x/i1
			j5 = j5/8
			paths.append(1)
		else:
			j5 = j5-3
			paths.append(2)
		if x < 7:
			j5 = j5-6
			x = x-3
			x = x*j5
			paths.append(3)
		else:
			j5 = i1-6
			i1 = j5/i1
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))