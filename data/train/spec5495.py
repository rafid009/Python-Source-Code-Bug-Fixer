import numpy as np 

def function(x):

	v0 = 5
	j8 = 0
	paths = []
	try:
		if x < 6:
			j8 = 1-x
			j8 = j8-x
			v0 = v0*j8
			paths.append(1)
		else:
			x = x+4
			x = 7+x
			x = x/1
			paths.append(2)
		if j8 >= 7:
			x = 7-0
			paths.append(3)
		else:
			v0 = 5*v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))