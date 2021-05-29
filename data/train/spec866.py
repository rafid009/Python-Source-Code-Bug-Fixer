import numpy as np 

def function(x):

	r6 = x
	v8 = x
	paths = []
	try:
		if r6 <= 5:
			r6 = r6+7
			r6 = 2-r6
			paths.append(1)
		else:
			v8 = 8/r6
			x = 0/x
			v8 = 5-v8
			paths.append(2)
		if v8 >= 5:
			v8 = v8-3
			r6 = r6/9
			paths.append(3)
		else:
			x = 3/v8
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