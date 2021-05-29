import numpy as np 

def function(x):

	f1 = x
	v3 = x
	paths = []
	try:
		if x < 9:
			v3 = 1-v3
			f1 = f1+9
			paths.append(1)
		else:
			f1 = 8*2
			x = x-x
			f1 = 1+f1
			paths.append(2)
		if x > 5:
			v3 = f1*f1
			paths.append(3)
		else:
			f1 = 2/f1
			v3 = v3-7
			f1 = f1/3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		v3 = f1**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))