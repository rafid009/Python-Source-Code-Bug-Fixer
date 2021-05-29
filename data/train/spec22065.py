import numpy as np 

def function(x):

	j7 = 1
	f6 = x
	paths = []
	try:
		if x > 3:
			x = 0*f6
			paths.append(1)
		else:
			f6 = f6*4
			f6 = f6+5
			paths.append(2)
		if f6 < 0:
			j7 = f6-f6
			f6 = f6*4
			f6 = f6/4
			paths.append(3)
		else:
			x = 9-1
			x = x+x
			x = x/f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))