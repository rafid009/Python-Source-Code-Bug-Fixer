import numpy as np 

def function(x):

	f1 = 9
	v8 = x
	paths = []
	try:
		if x < 3:
			f1 = f1+6
			paths.append(1)
		else:
			f1 = f1/f1
			x = 4*v8
			paths.append(2)
		if f1 >= 5:
			x = x+f1
			x = x+0
			paths.append(3)
		else:
			v8 = 9+f1
			v8 = f1-x
			x = x*2
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