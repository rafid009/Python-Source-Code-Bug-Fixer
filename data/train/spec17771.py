import numpy as np 

def function(x):

	j3 = 0
	y5 = 2
	paths = []
	try:
		if y5 >= 8:
			j3 = 2+j3
			x = x*8
			paths.append(1)
		else:
			y5 = 8/2
			j3 = x+7
			x = 0+6
			paths.append(2)
		if j3 <= 9:
			j3 = y5/j3
			j3 = 2-7
			paths.append(3)
		else:
			y5 = x/y5
			j3 = 8*j3
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