import numpy as np 

def function(x):

	i2 = x
	v6 = 8
	paths = []
	try:
		if i2 >= 1:
			v6 = v6-i2
			i2 = i2-4
			paths.append(1)
		else:
			x = 9-2
			paths.append(2)
		if x < 8:
			x = 3+x
			v6 = x/v6
			paths.append(3)
		else:
			i2 = i2/6
			v6 = x*v6
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