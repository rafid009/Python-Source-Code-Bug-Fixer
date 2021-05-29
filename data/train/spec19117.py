import numpy as np 

def function(x):

	v8 = x
	f1 = 9
	paths = []
	try:
		if x >= 1:
			x = 2-x
			paths.append(1)
		else:
			v8 = 1*7
			paths.append(2)
		if v8 > 7:
			v8 = 9+v8
			v8 = v8+f1
			f1 = f1-7
			paths.append(3)
		else:
			f1 = 7/3
			f1 = 2-v8
			f1 = f1*2
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))