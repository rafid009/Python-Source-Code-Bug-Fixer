import numpy as np 

def function(x):

	o1 = 9
	j9 = x
	paths = []
	try:
		if o1 >= 9:
			x = x-o1
			o1 = 0/o1
			paths.append(1)
		else:
			o1 = j9*4
			x = o1*j9
			paths.append(2)
		if j9 < 9:
			x = 6+4
			paths.append(3)
		else:
			x = x*j9
			j9 = 9+8
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