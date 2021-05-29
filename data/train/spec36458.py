import numpy as np 

def function(x):

	v8 = x
	q5 = 0
	paths = []
	try:
		if q5 >= 4:
			v8 = 5*v8
			q5 = 9+5
			paths.append(1)
		else:
			x = v8+x
			paths.append(2)
		if x >= 3:
			q5 = q5-4
			paths.append(3)
		else:
			v8 = x-8
			v8 = 9+v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))