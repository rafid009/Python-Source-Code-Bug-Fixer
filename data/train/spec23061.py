import numpy as np 

def function(x):

	v8 = x
	r6 = 6
	paths = []
	try:
		if x >= 6:
			r6 = r6/4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 4:
			v8 = r6+v8
			paths.append(3)
		else:
			r6 = v8/x
			r6 = 8+r6
			x = x-8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))