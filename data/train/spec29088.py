import numpy as np 

def function(x):

	o3 = 8
	r9 = 1
	paths = []
	try:
		if r9 < 4:
			r9 = r9-5
			x = o3*1
			o3 = o3+7
			paths.append(1)
		else:
			x = x*4
			r9 = r9+3
			o3 = o3*r9
			paths.append(2)
		if x > 8:
			x = x/1
			r9 = x+r9
			paths.append(3)
		else:
			o3 = 4*3
			o3 = o3-2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		o3 = r9**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))