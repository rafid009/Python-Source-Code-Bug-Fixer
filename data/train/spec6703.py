import numpy as np 

def function(x):

	y5 = 7
	k4 = 6
	paths = []
	try:
		if y5 <= 9:
			x = x+0
			y5 = 2-8
			k4 = k4*x
			paths.append(1)
		else:
			x = x*1
			k4 = k4+k4
			y5 = y5*9
			paths.append(2)
		if k4 >= 5:
			y5 = 6-y5
			k4 = k4*0
			paths.append(3)
		else:
			x = x+0
			k4 = k4*7
			k4 = 7+k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		y5 = k4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))