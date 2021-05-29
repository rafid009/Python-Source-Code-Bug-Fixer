import numpy as np 

def function(x):

	j3 = 8
	u5 = x
	paths = []
	try:
		if x >= 9:
			x = 1*x
			x = 2/x
			paths.append(1)
		else:
			j3 = u5+6
			u5 = u5+2
			x = x*2
			paths.append(2)
		if x < 3:
			x = x+9
			paths.append(3)
		else:
			u5 = 6/u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		j3 = u5**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))