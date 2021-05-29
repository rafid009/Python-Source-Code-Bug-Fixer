import numpy as np 

def function(x):

	y8 = 2
	j5 = 1
	paths = []
	try:
		if x < 5:
			j5 = x*3
			paths.append(1)
		else:
			j5 = j5/8
			j5 = j5-0
			paths.append(2)
		if y8 < 9:
			x = 4*x
			x = 3-1
			paths.append(3)
		else:
			j5 = 4+x
			x = 0*8
			x = x/j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		y8 = j5**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))