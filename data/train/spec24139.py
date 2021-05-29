import numpy as np 

def function(x):

	v8 = x
	n4 = x
	paths = []
	try:
		if n4 < 5:
			v8 = 1-v8
			paths.append(1)
		else:
			v8 = v8/9
			paths.append(2)
		if n4 <= 9:
			v8 = v8+v8
			paths.append(3)
		else:
			v8 = v8+5
			v8 = x/8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		n4 = v8**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))