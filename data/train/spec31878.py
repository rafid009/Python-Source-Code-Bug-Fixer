import numpy as np 

def function(x):

	j9 = x
	v0 = x
	paths = []
	try:
		if v0 >= 5:
			j9 = j9/3
			x = 6+x
			x = 3*1
			paths.append(1)
		else:
			x = v0+3
			j9 = j9*1
			paths.append(2)
		if j9 > 9:
			v0 = 9+v0
			paths.append(3)
		else:
			j9 = j9/3
			v0 = 6+x
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