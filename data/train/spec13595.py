import numpy as np 

def function(x):

	o4 = 8
	v3 = x
	paths = []
	try:
		if x <= 4:
			x = x*3
			x = 0*6
			x = x-o4
			paths.append(1)
		else:
			x = 8*o4
			v3 = 1*v3
			paths.append(2)
		if v3 > 3:
			x = x*v3
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))