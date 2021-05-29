import numpy as np 

def function(x):

	t7 = x
	v8 = 7
	paths = []
	try:
		if x >= 7:
			x = v8*7
			paths.append(1)
		else:
			t7 = 5/t7
			v8 = v8-5
			x = 8/x
			paths.append(2)
		if t7 < 6:
			x = x*9
			x = 6*x
			paths.append(3)
		else:
			t7 = t7/2
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		v8 = t7**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))