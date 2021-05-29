import numpy as np 

def function(x):

	v8 = 2
	b1 = x
	paths = []
	try:
		if b1 >= 2:
			x = x+5
			paths.append(1)
		else:
			x = x/3
			x = x-8
			b1 = b1-9
			paths.append(2)
		if b1 <= 6:
			v8 = 6-v8
			v8 = v8-9
			paths.append(3)
		else:
			v8 = 8-b1
			x = x/1
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