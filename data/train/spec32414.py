import numpy as np 

def function(x):

	o8 = 8
	j6 = x
	paths = []
	try:
		if j6 < 5:
			o8 = x*o8
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if j6 < 3:
			j6 = j6*o8
			x = x+x
			x = 7+2
			paths.append(3)
		else:
			j6 = x-j6
			j6 = j6*x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))