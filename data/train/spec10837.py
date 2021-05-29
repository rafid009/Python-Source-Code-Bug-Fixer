import numpy as np 

def function(x):

	u3 = x
	v0 = x
	paths = []
	try:
		if v0 < 4:
			v0 = 5-u3
			paths.append(1)
		else:
			u3 = u3/x
			u3 = 3+u3
			x = 5*5
			paths.append(2)
		if x > 5:
			v0 = u3*v0
			paths.append(3)
		else:
			v0 = u3/v0
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