import numpy as np 

def function(x):

	v6 = x
	u2 = 1
	paths = []
	try:
		if v6 < 9:
			u2 = v6-x
			x = 5-7
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if v6 <= 6:
			v6 = v6-9
			v6 = v6-4
			paths.append(3)
		else:
			v6 = 3+v6
			v6 = 3-v6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))