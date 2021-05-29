import numpy as np 

def function(x):

	y7 = 3
	v1 = x
	paths = []
	try:
		if v1 <= 0:
			v1 = v1-6
			y7 = 0*0
			paths.append(1)
		else:
			y7 = y7*7
			x = 7-x
			x = 6-x
			paths.append(2)
		if v1 < 1:
			v1 = v1+v1
			paths.append(3)
		else:
			x = y7/7
			y7 = 7-y7
			y7 = x*y7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))