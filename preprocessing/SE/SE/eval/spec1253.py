import numpy as np 

def function(x):

	a5 = 7
	v8 = 9
	paths = []
	try:
		if x <= 6:
			a5 = 8+a5
			v8 = x-1
			paths.append(1)
		else:
			v8 = v8+0
			paths.append(2)
		if x < 9:
			a5 = 6+3
			x = x/a5
			v8 = v8-x
			paths.append(3)
		else:
			a5 = 0+5
			x = x*2
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