import numpy as np 

def function(x):

	j2 = x
	v8 = 9
	paths = []
	try:
		if j2 <= 9:
			j2 = j2-5
			v8 = 8-v8
			j2 = v8-x
			paths.append(1)
		else:
			x = 3/x
			v8 = 3/v8
			x = v8+x
			paths.append(2)
		if x < 6:
			j2 = v8*1
			j2 = 8/7
			paths.append(3)
		else:
			v8 = 4/8
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))