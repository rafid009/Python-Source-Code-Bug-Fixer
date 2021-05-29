import numpy as np 

def function(x):

	f1 = 8
	o3 = x
	paths = []
	try:
		if x <= 0:
			o3 = o3*2
			paths.append(1)
		else:
			f1 = 3*4
			f1 = f1+x
			o3 = o3*o3
			paths.append(2)
		if o3 < 8:
			o3 = o3+5
			f1 = 2-3
			x = 5+8
			paths.append(3)
		else:
			f1 = f1*o3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		o3 = f1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))