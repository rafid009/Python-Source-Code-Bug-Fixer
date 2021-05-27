import numpy as np 

def function(x):

	f8 = x
	v8 = 6
	paths = []
	try:
		if v8 < 4:
			x = x+6
			paths.append(1)
		else:
			v8 = v8-3
			v8 = v8*v8
			paths.append(2)
		if v8 <= 0:
			f8 = f8*1
			f8 = x+7
			f8 = 0/4
			paths.append(3)
		else:
			v8 = 9*1
			v8 = v8*v8
			x = f8/f8
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))