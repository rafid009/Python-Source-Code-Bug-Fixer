import numpy as np 

def function(x):

	n7 = x
	j3 = 2
	paths = []
	try:
		if x >= 4:
			x = x+x
			j3 = j3+x
			n7 = n7-2
			paths.append(1)
		else:
			j3 = n7+j3
			paths.append(2)
		if j3 <= 4:
			x = 4-0
			paths.append(3)
		else:
			n7 = n7-1
			x = x-n7
			n7 = n7/x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))