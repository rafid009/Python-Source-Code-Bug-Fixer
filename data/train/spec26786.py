import numpy as np 

def function(x):

	v0 = x
	b1 = x
	x = x
	paths = []
	try:
		if v0 < 7:
			v0 = x/3
			x = 1-b1
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if b1 < 0:
			x = 0-x
			v0 = 6*x
			paths.append(3)
		else:
			b1 = v0+3
			b1 = x+0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))