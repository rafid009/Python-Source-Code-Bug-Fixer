import numpy as np 

def function(x):

	v6 = x
	i9 = x
	paths = []
	try:
		if x <= 9:
			x = 8/3
			i9 = v6/6
			x = 7+x
			paths.append(1)
		else:
			x = x*6
			v6 = v6*6
			i9 = i9+i9
			paths.append(2)
		if v6 > 0:
			v6 = 8/v6
			x = x+1
			x = x+7
			paths.append(3)
		else:
			i9 = i9+v6
			i9 = v6+7
			x = 5+i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))