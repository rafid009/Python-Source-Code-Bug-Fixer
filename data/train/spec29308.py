import numpy as np 

def function(x):

	x5 = x
	v8 = 5
	paths = []
	try:
		if x <= 6:
			v8 = v8*7
			x = 6+9
			x5 = x5*5
			paths.append(1)
		else:
			x5 = x5+x5
			x5 = x5-x5
			paths.append(2)
		if v8 < 5:
			v8 = 3*v8
			x5 = x5+5
			x5 = x5*2
			paths.append(3)
		else:
			v8 = x5/v8
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x5 = v8**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))