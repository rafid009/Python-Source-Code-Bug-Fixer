import numpy as np 

def function(x):

	v3 = x
	f6 = x
	paths = []
	try:
		if v3 > 7:
			f6 = 6*6
			paths.append(1)
		else:
			v3 = 6/x
			x = x-2
			paths.append(2)
		if f6 < 9:
			x = x+v3
			paths.append(3)
		else:
			f6 = f6/6
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		f6 = v3**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))