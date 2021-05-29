import numpy as np 

def function(x):

	v1 = 3
	f3 = 9
	paths = []
	try:
		if f3 <= 3:
			v1 = v1*f3
			x = x*5
			paths.append(1)
		else:
			v1 = v1-f3
			f3 = f3*1
			f3 = v1*8
			paths.append(2)
		if f3 < 3:
			f3 = x*f3
			f3 = v1/6
			paths.append(3)
		else:
			f3 = 5*v1
			x = 4/x
			v1 = v1*1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))