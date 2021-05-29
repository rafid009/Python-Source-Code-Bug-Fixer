import numpy as np 

def function(x):

	n7 = 1
	v6 = x
	paths = []
	try:
		if x <= 0:
			x = v6-5
			v6 = n7*v6
			paths.append(1)
		else:
			v6 = 9/v6
			v6 = 2/3
			paths.append(2)
		if v6 > 6:
			n7 = n7/5
			n7 = n7*n7
			n7 = v6*n7
			paths.append(3)
		else:
			x = x+v6
			x = x/1
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