import numpy as np 

def function(x):

	u1 = x
	v0 = x
	paths = []
	try:
		if u1 < 8:
			x = x+5
			u1 = 7*3
			v0 = 2+v0
			paths.append(1)
		else:
			v0 = v0*7
			u1 = 8+u1
			v0 = v0/8
			paths.append(2)
		if u1 >= 3:
			u1 = 4+x
			x = 2*x
			x = v0-x
			paths.append(3)
		else:
			x = 0+x
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