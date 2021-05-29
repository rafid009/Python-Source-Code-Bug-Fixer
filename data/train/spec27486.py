import numpy as np 

def function(x):

	g4 = 4
	v8 = x
	x = 1
	paths = []
	try:
		if x <= 7:
			x = x-5
			g4 = v8+1
			paths.append(1)
		else:
			x = 9/5
			v8 = v8*8
			paths.append(2)
		if x >= 3:
			g4 = g4+2
			paths.append(3)
		else:
			v8 = v8*2
			x = x-v8
			g4 = g4+2
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