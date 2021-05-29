import numpy as np 

def function(x):

	v8 = x
	q9 = x
	paths = []
	try:
		if q9 <= 3:
			x = x+5
			x = 0+x
			x = x-5
			paths.append(1)
		else:
			v8 = q9*6
			v8 = v8-7
			paths.append(2)
		if v8 <= 2:
			q9 = q9/q9
			x = q9-4
			paths.append(3)
		else:
			v8 = q9-1
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