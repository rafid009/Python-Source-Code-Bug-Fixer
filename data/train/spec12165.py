import numpy as np 

def function(x):

	u3 = x
	v3 = 5
	paths = []
	try:
		if u3 >= 3:
			v3 = 2+2
			x = x+v3
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if u3 >= 3:
			u3 = 0-0
			paths.append(3)
		else:
			v3 = x/2
			v3 = v3/8
			u3 = u3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))