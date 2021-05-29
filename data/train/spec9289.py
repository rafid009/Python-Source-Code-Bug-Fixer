import numpy as np 

def function(x):

	v8 = 1
	t1 = 0
	x = x
	paths = []
	try:
		if x > 9:
			v8 = 5/v8
			paths.append(1)
		else:
			x = 0-0
			paths.append(2)
		if x < 3:
			t1 = 2+t1
			t1 = t1/8
			t1 = t1/2
			paths.append(3)
		else:
			v8 = t1-5
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