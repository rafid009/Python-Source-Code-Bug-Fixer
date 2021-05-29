import numpy as np 

def function(x):

	f8 = 6
	v5 = 7
	paths = []
	try:
		if x >= 5:
			v5 = 0+v5
			x = x-v5
			paths.append(1)
		else:
			x = x-f8
			f8 = f8+f8
			v5 = x*v5
			paths.append(2)
		if f8 < 3:
			x = x/2
			v5 = 4-v5
			paths.append(3)
		else:
			x = x/9
			v5 = v5-0
			f8 = 5-f8
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))