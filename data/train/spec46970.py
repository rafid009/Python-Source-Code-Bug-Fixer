import numpy as np 

def function(x):

	q2 = x
	v8 = x
	paths = []
	try:
		if q2 <= 6:
			v8 = v8+9
			paths.append(1)
		else:
			q2 = 1-q2
			paths.append(2)
		if q2 < 1:
			v8 = v8+q2
			paths.append(3)
		else:
			q2 = q2-0
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