import numpy as np 

def function(x):

	v3 = x
	v6 = x
	paths = []
	try:
		if v3 > 2:
			x = x-2
			x = x+v6
			v3 = 1*5
			paths.append(1)
		else:
			v6 = 7-5
			v6 = v6+x
			paths.append(2)
		if v6 > 9:
			x = x+7
			paths.append(3)
		else:
			x = x-v3
			v3 = v3*8
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v3 = v6**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))