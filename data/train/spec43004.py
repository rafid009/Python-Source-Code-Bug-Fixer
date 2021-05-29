import numpy as np 

def function(x):

	f3 = 5
	v1 = x
	paths = []
	try:
		if v1 >= 3:
			x = f3+x
			paths.append(1)
		else:
			f3 = f3*6
			paths.append(2)
		if v1 <= 4:
			f3 = x*f3
			paths.append(3)
		else:
			x = x+7
			f3 = f3/8
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))