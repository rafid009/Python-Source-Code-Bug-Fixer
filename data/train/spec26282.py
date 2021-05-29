import numpy as np 

def function(x):

	v8 = x
	j8 = x
	paths = []
	try:
		if x <= 0:
			v8 = 3+v8
			paths.append(1)
		else:
			x = 3+3
			v8 = v8-5
			v8 = v8+j8
			paths.append(2)
		if j8 > 4:
			v8 = v8*3
			x = x-x
			paths.append(3)
		else:
			j8 = j8+j8
			x = x*5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		v8 = j8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))