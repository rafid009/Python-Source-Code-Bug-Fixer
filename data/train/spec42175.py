import numpy as np 

def function(x):

	v8 = 0
	n9 = x
	paths = []
	try:
		if x >= 0:
			x = v8+x
			n9 = 9*8
			v8 = v8*x
			paths.append(1)
		else:
			x = x/8
			n9 = 2/7
			paths.append(2)
		if n9 < 7:
			v8 = x/n9
			paths.append(3)
		else:
			x = 7*x
			v8 = v8*x
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