import numpy as np 

def function(x):

	r2 = 6
	v4 = x
	paths = []
	try:
		if r2 <= 2:
			v4 = v4/6
			paths.append(1)
		else:
			v4 = 4+v4
			v4 = 0+v4
			paths.append(2)
		if v4 <= 2:
			x = 2+8
			x = r2+v4
			paths.append(3)
		else:
			v4 = r2+5
			v4 = r2*1
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))