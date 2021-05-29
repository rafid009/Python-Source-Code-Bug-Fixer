import numpy as np 

def function(x):

	f9 = x
	i2 = x
	paths = []
	try:
		if x < 4:
			f9 = i2-f9
			i2 = i2+7
			i2 = x-6
			paths.append(1)
		else:
			f9 = i2+f9
			paths.append(2)
		if x <= 7:
			f9 = 1-f9
			f9 = i2/i2
			i2 = f9+9
			paths.append(3)
		else:
			f9 = 0-6
			i2 = i2+x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		i2 = f9**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))