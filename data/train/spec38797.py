import numpy as np 

def function(x):

	g5 = x
	v6 = 0
	paths = []
	try:
		if v6 > 9:
			v6 = v6-7
			x = x-4
			x = 3+x
			paths.append(1)
		else:
			v6 = v6*5
			v6 = v6/x
			v6 = v6+7
			paths.append(2)
		if v6 < 0:
			v6 = x/x
			v6 = v6/3
			paths.append(3)
		else:
			x = x+3
			v6 = v6/4
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		v6 = g5**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))