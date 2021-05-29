import numpy as np 

def function(x):

	o2 = x
	j7 = x
	paths = []
	try:
		if x >= 4:
			x = 8-x
			paths.append(1)
		else:
			x = 5+x
			j7 = j7*1
			paths.append(2)
		if j7 < 3:
			j7 = x+j7
			o2 = o2+j7
			paths.append(3)
		else:
			j7 = j7-x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))