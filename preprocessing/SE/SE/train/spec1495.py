import numpy as np 

def function(x):

	r5 = x
	v9 = 4
	paths = []
	try:
		if r5 < 1:
			v9 = x/9
			r5 = 0+2
			paths.append(1)
		else:
			v9 = 7-v9
			x = x*3
			r5 = x*r5
			paths.append(2)
		if r5 < 2:
			x = x/1
			v9 = v9/v9
			paths.append(3)
		else:
			x = x+r5
			v9 = 4*v9
			x = r5/x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))