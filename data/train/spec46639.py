import numpy as np 

def function(x):

	j9 = x
	v0 = 0
	paths = []
	try:
		if x <= 6:
			v0 = x*j9
			x = j9+7
			j9 = 8*3
			paths.append(1)
		else:
			j9 = j9*1
			v0 = 6*0
			x = x/5
			paths.append(2)
		if x >= 9:
			j9 = 2/j9
			x = x+8
			j9 = 8-5
			paths.append(3)
		else:
			v0 = v0+x
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))