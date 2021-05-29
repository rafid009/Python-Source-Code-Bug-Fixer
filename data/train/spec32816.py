import numpy as np 

def function(x):

	v3 = x
	f8 = 8
	paths = []
	try:
		if x >= 8:
			v3 = v3+9
			paths.append(1)
		else:
			x = x/f8
			v3 = v3-7
			paths.append(2)
		if x > 9:
			v3 = x/f8
			paths.append(3)
		else:
			f8 = f8+7
			v3 = v3/8
			x = x/2
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		f8 = v3**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))