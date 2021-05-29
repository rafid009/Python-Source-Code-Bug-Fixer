import numpy as np 

def function(x):

	f1 = x
	v8 = x
	paths = []
	try:
		if f1 <= 4:
			f1 = f1+x
			v8 = v8-0
			x = v8-x
			paths.append(1)
		else:
			x = 6+1
			v8 = v8+5
			paths.append(2)
		if v8 <= 2:
			f1 = f1+5
			v8 = v8-0
			paths.append(3)
		else:
			x = x+3
			x = 7+x
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