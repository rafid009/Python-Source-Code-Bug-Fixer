import numpy as np 

def function(x):

	a8 = x
	v8 = 2
	paths = []
	try:
		if x > 0:
			v8 = 9*9
			x = x+5
			paths.append(1)
		else:
			x = 9-x
			x = 6*2
			x = 5*x
			paths.append(2)
		if v8 > 5:
			x = 9*x
			a8 = 2-8
			paths.append(3)
		else:
			v8 = 6/a8
			v8 = x*0
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		v8 = a8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))