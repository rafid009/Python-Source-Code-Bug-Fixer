import numpy as np 

def function(x):

	v2 = x
	u1 = x
	paths = []
	try:
		if v2 <= 8:
			x = v2*x
			x = 2*x
			v2 = v2+v2
			paths.append(1)
		else:
			u1 = x-0
			paths.append(2)
		if x > 4:
			x = 2+v2
			v2 = x+2
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))