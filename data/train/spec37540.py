import numpy as np 

def function(x):

	f0 = x
	v8 = x
	paths = []
	try:
		if f0 <= 8:
			x = f0*x
			paths.append(1)
		else:
			f0 = 5/f0
			paths.append(2)
		if v8 < 4:
			v8 = 4/3
			v8 = x-v8
			x = 0*x
			paths.append(3)
		else:
			x = x/6
			v8 = 9-9
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))