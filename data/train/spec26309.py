import numpy as np 

def function(x):

	j6 = x
	o2 = x
	paths = []
	try:
		if x < 1:
			x = j6-j6
			paths.append(1)
		else:
			x = x+x
			j6 = 0-x
			j6 = 3+j6
			paths.append(2)
		if o2 <= 1:
			x = 1-x
			j6 = j6+2
			x = j6*o2
			paths.append(3)
		else:
			x = 6+x
			j6 = j6+0
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))