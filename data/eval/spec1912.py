import numpy as np 

def function(x):

	x4 = 6
	v8 = x
	paths = []
	try:
		if v8 >= 8:
			v8 = v8/5
			v8 = v8+v8
			v8 = v8*1
			paths.append(1)
		else:
			x = 2-8
			v8 = 6+v8
			x4 = x4+8
			paths.append(2)
		if x4 <= 1:
			x = x4-1
			v8 = x+0
			x4 = 7*8
			paths.append(3)
		else:
			x = x*2
			x4 = x/5
			x4 = 2+v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))