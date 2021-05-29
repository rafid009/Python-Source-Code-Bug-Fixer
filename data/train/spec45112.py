import numpy as np 

def function(x):

	j6 = x
	v0 = 4
	x = x
	paths = []
	try:
		if x < 0:
			x = x*9
			x = 0-8
			j6 = j6/v0
			paths.append(1)
		else:
			v0 = v0/3
			x = 6*x
			j6 = j6/x
			paths.append(2)
		if v0 >= 6:
			v0 = v0*8
			j6 = j6+j6
			x = 3*0
			paths.append(3)
		else:
			x = x-7
			x = v0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))