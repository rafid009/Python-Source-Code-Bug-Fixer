import numpy as np 

def function(x):

	v2 = 6
	a7 = 4
	paths = []
	try:
		if v2 < 5:
			a7 = a7+6
			x = 1+6
			x = 6+v2
			paths.append(1)
		else:
			v2 = v2+v2
			a7 = a7+7
			a7 = a7+x
			paths.append(2)
		if x > 0:
			a7 = 6-9
			a7 = a7*v2
			v2 = 1*a7
			paths.append(3)
		else:
			x = a7+6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		v2 = a7**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))