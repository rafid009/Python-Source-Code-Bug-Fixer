import numpy as np 

def function(x):

	j3 = x
	r4 = 0
	paths = []
	try:
		if x <= 0:
			j3 = 1-j3
			r4 = r4*9
			x = 7+5
			paths.append(1)
		else:
			x = 0/x
			r4 = r4-5
			paths.append(2)
		if x < 9:
			r4 = r4-4
			j3 = x*6
			paths.append(3)
		else:
			r4 = 0+6
			r4 = x+r4
			x = x+7
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))