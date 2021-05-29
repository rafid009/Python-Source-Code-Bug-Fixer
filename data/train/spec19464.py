import numpy as np 

def function(x):

	v0 = x
	e3 = 0
	paths = []
	try:
		if e3 >= 3:
			e3 = e3/x
			x = 9/x
			x = 6+4
			paths.append(1)
		else:
			e3 = e3*9
			e3 = v0/4
			x = x/3
			paths.append(2)
		if x <= 7:
			e3 = e3*6
			e3 = v0*3
			paths.append(3)
		else:
			x = x+7
			x = 4+9
			e3 = e3-1
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