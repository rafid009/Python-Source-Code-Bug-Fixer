import numpy as np 

def function(x):

	v3 = 9
	v8 = x
	paths = []
	try:
		if v3 < 0:
			v8 = x+v8
			v3 = 0-8
			x = 4*x
			paths.append(1)
		else:
			v8 = v8/7
			v3 = x+v3
			paths.append(2)
		if v3 > 5:
			v8 = v3/3
			x = v8-x
			v3 = v3+v8
			paths.append(3)
		else:
			v8 = x*1
			x = 4-4
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v8 = v3**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))