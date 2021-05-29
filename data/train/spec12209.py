import numpy as np 

def function(x):

	v0 = 4
	v8 = x
	paths = []
	try:
		if v8 > 7:
			v0 = 6-v0
			paths.append(1)
		else:
			x = x+v8
			paths.append(2)
		if x > 3:
			v0 = v0-7
			x = x/2
			paths.append(3)
		else:
			v0 = v0+v8
			x = 2*4
			x = x*4
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