import numpy as np 

def function(x):

	u3 = x
	v1 = 4
	paths = []
	try:
		if v1 < 2:
			v1 = v1*0
			paths.append(1)
		else:
			u3 = 5/u3
			paths.append(2)
		if u3 > 2:
			u3 = u3-4
			x = x+9
			paths.append(3)
		else:
			v1 = v1-6
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))